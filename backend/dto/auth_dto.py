from pydantic import BaseModel

class AuthConfirm(BaseModel):
    token: str
    telegram_id: int