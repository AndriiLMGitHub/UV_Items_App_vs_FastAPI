from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from database.engine import get_db


SessionDependency = Annotated[AsyncSession, Depends(get_db)]