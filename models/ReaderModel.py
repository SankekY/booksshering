from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional
import uuid

class ReaderS(BaseModel):
    name: str = Field(None, min_length=3, description="Имя читателя (Обязательное)")
    email: EmailStr

class ReaderCreateS(ReaderS):
    reader_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Автоматически генерируемый ID")