from sqlalchemy import select

from apps.exceptions import ItemNotFoundError
from apps.models import Item
from apps.schemas import ItemCreate
from database.dependencies import SessionDependency


async def get_all_items(session: SessionDependency):
    # Code to retrieve all items from the database using the session
    stmt = select(Item)
    items = await session.execute(stmt)
    items = items.scalars().all()
    return items

async def create_item(session: SessionDependency, item_data: ItemCreate):
    # Code to create an item in the database using the session
    new_item = Item(**item_data.model_dump())
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)

    return new_item


async def get_item_by_id(session: SessionDependency, item_id: int):
    stmt = select(Item).where(Item.id == item_id)
    result = await session.execute(stmt)
    
    # Витягуємо сутність
    item = result.scalar_one_or_none()
    
    # Тільки тепер перевіряємо
    if not item:
        raise ItemNotFoundError(item_id=item_id)
        
    return item


async def delete_item(session: SessionDependency, item_id: int):
    # Code to delete an item by ID from the database using the session
    stmt = select(Item).where(Item.id == item_id)
    item = await session.execute(stmt)
    item = item.scalar_one_or_none()
    if not item:
        raise ItemNotFoundError(item_id=item_id)
    await session.delete(item)
    await session.commit()
    return True
