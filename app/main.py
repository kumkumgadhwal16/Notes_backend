from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers import auth, notes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Development setup only.
    # in Production  Alembic migrations use
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Notes App API",
    
    description="Secure Notes App backend built with FastAPI and PostgreSQL",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth.router)
app.include_router(notes.router)


@app.get("/", tags=["Health"])
def health_check():
    return {"message": "Notes App API is running"}
