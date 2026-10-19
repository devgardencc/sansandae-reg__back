from pydantic import BaseModel
from datetime import datetime


class RegisterRequest(BaseModel):
    name: str
    phone: str
    tg: str
    club: bool
    photo: bool
    mountain: str
    date: str


class RegisterResponse(BaseModel):
    name: str
    created_at: datetime


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
