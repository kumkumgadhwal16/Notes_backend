
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import models
from app.database import get_db
from app.dependencies import get_current_user
from app.schemas import NoteCreate, NoteUpdate, NoteResponse


router = APIRouter(prefix="/notes", tags=["Notes"])



def find_my_note(
    note_id: int,
    user_id: int,
    db: Session,
) -> models.Note:
    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.user_id == user_id,
    ).first()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        )

    return note


@router.post(
    "",
    response_model=NoteResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_note(
    data: NoteCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    note = models.Note(
        title=data.title.strip() if data.title else None,
        content=data.content,
        user_id=user.id,
    )

    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.get("", response_model=list[NoteResponse])
def list_notes(
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    return (
        db.query(models.Note)
        .filter(models.Note.user_id == user.id)
        .order_by(models.Note.id.desc())
        .all()
    )


@router.get("/{note_id}", response_model=NoteResponse)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    return find_my_note(note_id, user.id, db)


# @router.patch("/{note_id}", response_model=NoteResponse)
# def update_note(
#     note_id: int,
#     data: NoteUpdate,
#     db: Session = Depends(get_db),
#     user: models.User = Depends(get_current_user),
# ):
#     # Find logged-in user's note
#     note = find_my_note(note_id, user.id, db)

#     # Get fields provided by user
#     changes = data.model_dump(exclude_unset=True)

#     if not changes:
#         raise HTTPException(
#             status_code=400,
#             detail="Please provide data to update"
#         )

#     if "content" in changes:
#         if changes["content"] is None or not changes["content"].strip():
#             raise HTTPException(
#                 status_code=422,
#                 detail="Content cannot be empty"
#             )

#     if "title" in changes and changes["title"] is not None:
#         changes["title"] = changes["title"].strip() or None

#     # Update note
#     for field, value in changes.items():
#         setattr(note, field, value)

#     db.commit()
#     db.refresh(note)

#     return note

@router.patch("/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: int,
    data: NoteUpdate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    note = find_my_note(note_id, user.id, db)
    changes = data.model_dump(exclude_unset=True)

    if "content" in changes and changes["content"] is None:
     raise HTTPException(
        status_code=422,
        detail="Note content cannot be null",
    )

    if not changes:
        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update",
        )

    if "title" in changes and changes["title"] is not None:
        changes["title"] = changes["title"].strip() or None

    for field, value in changes.items():
        setattr(note, field, value)

    db.commit()
    db.refresh(note)
    return note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    note = find_my_note(note_id, user.id, db)
    db.delete(note)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


