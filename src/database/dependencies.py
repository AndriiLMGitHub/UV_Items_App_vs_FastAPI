from fastapi import Depends
from typing import Annotated

from database.engine import AsyncSessionLocal, get_db


SessionDependency = Annotated[AsyncSessionLocal, Depends(get_db)]