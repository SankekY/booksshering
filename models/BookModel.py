from pydantic import BaseModel, Field, field_validator
from typing import Optional
import uuid

class BookS(BaseModel):
    title: str = Field(None, min_length=1, description="Название книги (обязательное)")
    author: str = Field(None, min_length=1, description="Автор книги (обязательное)")
    publication_year: Optional[int] = Field(None, ge=0, le=2023, description="Год публикации (необязательное)")
    isbn: Optional[str] = Field(
        None, 
        min_length=10, 
        max_length=17, 
        pattern=r'^[0-9\-]+$', 
        description="ISBN (уникальный, необязательное)"
    )
    copies: int = Field(
        default=1, 
        ge=0, 
        description="Количество экземпляров (по умолчанию 1, не может быть меньше 0)"
    )

    @field_validator('publication_year')
    def validate_publication_year(cls, v):
        if v is not None and (v < 0 or v > 2023):
            raise ValueError('Год публикации должен быть между 0 и 2023')
        return v
    
class BookDB(BookS):
    book_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Автоматически генерируемый ID")