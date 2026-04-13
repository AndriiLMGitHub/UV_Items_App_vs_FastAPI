from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    title: str
    description: str = None
    user_id: int

class ItemResponse(BaseModel):
    success: bool = True
    data: Item


class ListItemResponse(BaseModel):
    success: bool = True
    data: List[Item]


class ItemCreate(BaseModel):
    title: str
    description: str = None
    user_id: int
