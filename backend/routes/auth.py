
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.services.auth_service import confirm_auth, start_auth
from data.database import get_db
from dto.auth_dto import AuthConfirm

router = APIRouter()


@router.post("/v1/auth/start")
def start(db: Session = Depends(get_db)):
    return start_auth(db)

@router.post('/v1/auth/confirm')
def confirm(dto: AuthConfirm,
    db: Session = Depends(get_db)):
    return confirm_auth(dto, db)
