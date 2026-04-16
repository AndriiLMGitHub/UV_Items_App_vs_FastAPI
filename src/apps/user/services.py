from sqlalchemy import select
from sqlalchemy.orm import selectinload

from apps.user.models import User
from apps.user.schemas import UserCreate
from database.dependencies import SessionDependency


async def get_all_users_service(session: SessionDependency):
   
    stmt = select(User).options(selectinload(User.items))
    result = await session.execute(stmt)
    users = result.scalars().all()

    return users


async def create_user_service(session: SessionDependency, user_data: UserCreate):
    # Code to create a user in the database using the session
    new_user = User(**user_data.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user
    