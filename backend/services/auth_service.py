import secrets
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
from data.models import AuthSession, User
from dto.auth_dto import AuthConfirm


def start_auth(db: Session):
    token = secrets.token_urlsafe(32)

    session = AuthSession(
        token=token,
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=5)
    )

    db.add(session)
    db.commit()

    return {"token": token}

def confirm_auth(dto: AuthConfirm, db: Session):
    auth_session = db.scalar(
            select(AuthSession)
            .where(AuthSession.token == dto.token)
        )
    if auth_session is None:
        raise HTTPException(
            status_code=404,
            detail='Auth session not found'
        )
    
    if auth_session.expires_at < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=400,
            detail='Auth session expired'
        )

    auth_session.telegram_id = dto.telegram_id
    
    user = db.scalar(
        select(User).where(
            User.telegram_id == dto.telegram_id
        )
    )
    
    if user is None:
        user = User(
            telegram_id = dto.telegram_id
        )
        db.add(user)
    db.commit()
    return {'status': 'confirm'}
