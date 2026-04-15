from datetime import datetime
from typing import Optional, TYPE_CHECKING
from database.base import Base

from sqlalchemy import String, func
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

# Цей блок виконується ТІЛЬКИ для IDE та лінтерів. 
# Під час реального запуску FastAPI Python ігнорує його.
if TYPE_CHECKING:
    from apps.items.models import Item

class User(Base):
    __tablename__ = "users"
    
    # primary_key вже гарантує індексацію.
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # unique=True вже є індексом. Обмежуємо довжину рядків для оптимізації.
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    
    full_name: Mapped[Optional[str]] = mapped_column(String(100), index=True)
    
    # server_default гарантує, що БД сама підставить значення, навіть якщо запис 
    # буде створено не через SQLAlchemy (наприклад, прямим SQL-запитом або міграцією).
    is_active: Mapped[bool] = mapped_column(default=True, server_default="true")
    is_superuser: Mapped[bool] = mapped_column(default=False, server_default="false")
    
    # Дати - це datetime. Генеруються базою даних автоматично.
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        onupdate=func.now()
    )
    
    last_login: Mapped[Optional[datetime]] = mapped_column(index=True)


    # Зворотний ORM-зв'язок. 
    # cascade="all, delete-orphan" дублює логіку каскадного видалення на рівні ORM.
    items: Mapped[list["Item"]] = relationship(
        back_populates="owner", 
        cascade="all, delete-orphan"
    )