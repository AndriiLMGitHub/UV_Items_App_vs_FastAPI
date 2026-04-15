from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from apps.items.schemas import Item  # Імпортуємо схему Item, щоб включити її у UserSchema

# 2. Базова схема (поля, які є скрізь)
class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None  # Або str | None = None для Python 3.10+

# 3. Схема для СТВОРЕННЯ (вхідні дані)
class UserCreate(UserBase):
    # Тут зазвичай ще додається password
    username: str
    email: str
    full_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

# 4. Схема для ВІДДАЧІ (те, що йде клієнту)
class UserSchema(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None
    
    # Включаємо зв'язок. За замовчуванням порожній масив.
    items: List[Item] = []

    # КРИТИЧНО: без цього Pydantic не прочитає об'єкт SQLAlchemy
    model_config = ConfigDict(from_attributes=True)

# 5. Схеми відповідей (Wrappers)
class UserItemResponse(BaseModel):
    message: str
    data: UserSchema

class UsersListResponse(BaseModel):
    message: str
    data: List[UserSchema]