from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column



from .database import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str | None] = mapped_column(String(100))

class AuthSession(Base):
    __tablename__ = 'auth_sessions'

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(String(64), unique=True)
    telegram_id: Mapped[int | None]
    expires_at: Mapped[datetime]