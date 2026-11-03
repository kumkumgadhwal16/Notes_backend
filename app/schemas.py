
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr

    model_config = {"from_attributes": True}



class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"




class NoteResponse(BaseModel):
    id: int
    title: str | None
    content: str
    user_id: int
    owner: UserResponse

    model_config = {"from_attributes": True}    


class NoteCreate(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    content: str = Field(min_length=1)


class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    content: str | None = Field(default=None, min_length=1)