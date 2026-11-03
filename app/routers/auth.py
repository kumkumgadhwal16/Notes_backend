
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app import models
from app.database import get_db
from app.schemas import UserCreate, UserLogin, UserResponse, TokenResponse
from app.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    email = str(user_data.email).lower()

    existing_user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email is already registered",
        )

    user = models.User(
        first_name=user_data.first_name.strip(),
        last_name=user_data.last_name.strip(),
        email=email,
        hashed_password=hash_password(user_data.password),
    )

    db.add(user)

    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email is already registered",
        )

    return user


@router.post("/login", response_model=TokenResponse)
def login_user(
    credentials: UserLogin,
    db: Session = Depends(get_db),
):
    email = str(credentials.email).lower()

    user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if user is None or not verify_password(
        credentials.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "access_token": create_access_token(user.id),
        "token_type": "bearer",
    }
