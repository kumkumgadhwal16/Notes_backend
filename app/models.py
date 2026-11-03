from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )
    hashed_password: Mapped[str] = mapped_column(String(255))

    notes: Mapped[list["Note"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )
    content: Mapped[str] = mapped_column(Text)

   


    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    owner: Mapped["User"] = relationship(back_populates="notes")