from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

if TYPE_CHECKING:
    from apps.user.models import User


class Item(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(255), index=True)

    # 1. Зовнішній ключ на таблицю users. 
    # index=True важливий, бо ми часто будемо шукати айтеми конкретного юзера.
    # ondelete="CASCADE" гарантує цілісність на рівні БД (якщо юзер видаляється - БД сама видалить його айтеми).
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    
    # 2. ORM-зв'язок. Дозволяє звертатися до item.owner
    owner: Mapped["User"] = relationship(back_populates="items")



