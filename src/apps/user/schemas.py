from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from apps.items.schemas import Item  # Переконайся, що імпорт коректний

# 1. Базова схема (поля, які є скрізь)
class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None



# 2. Схема для СТВОРЕННЯ (вхідні дані)
class UserCreate(UserBase):
    # Тут залишаться лише ті поля, яких немає в UserBase (наприклад, password).
    # Поля username, email та full_name вже успадковані.
    pass 
    # model_config тут не потрібен, бо це схема для парсингу вхідного JSON

# 3. Базова схема для ВІДДАЧІ (те, що йде клієнту в загальних списках)
# Вона НЕ містить зв'язків (items), щоб уникнути помилки MissingGreenlet
class UserSchema(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None

    # КРИТИЧНО: дозволяє Pydantic читати об'єкт SQLAlchemy
    model_config = ConfigDict(from_attributes=True)

# 4. Детальна схема для ВІДДАЧІ (для ендпоінту отримання одного юзера)
# Вона успадковує всі поля з UserSchema і додає зв'язки
class UserDetailSchema(UserSchema):
    items: List[Item] = []

# 5. Схеми відповідей (Wrappers)

# Використовується для GET /users/ (список юзерів)
class UsersListResponse(BaseModel):
    message: str
    data: List[UserSchema]  # Використовує схему БЕЗ items

# Використовується для GET /users/{id} та POST /users/
class UserItemResponse(BaseModel):
    message: str
    data: UserDetailSchema  # Використовує схему ЗІ зв'язками items


# Додай це до розділу "Схеми відповідей"
class UserCreateResponse(BaseModel):
    message: str
    data: UserSchema  # Використовуємо базову схему БЕЗ items