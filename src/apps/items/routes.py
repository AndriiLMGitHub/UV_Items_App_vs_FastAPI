from typing import Annotated

from fastapi import APIRouter, Depends

from apps.items.schemas import ItemCreate, ItemResponse, ListItemResponse
from apps.items.services import create_item, delete_item, get_all_items, get_item_by_id
from database.dependencies import SessionDependency

router = APIRouter(
    prefix="/api/items",
    tags=["API Items Endpoints"]
)


@router.get("/", response_model=ListItemResponse, summary="Get all items", description="Endpoint to retrieve all items.")
async def get_all_items_router(session: SessionDependency):
    items = await get_all_items(session)
    return {"message": "Items retrieved successfully", "data": items}


@router.post("/", response_model=ItemResponse, summary="Create an item", description="Endpoint to create a new item.")
async def create_item_router(session: SessionDependency, item_data: Annotated[ItemCreate, Depends()]):
    new_item = await create_item(session, item_data)
    return {"message": "Item created successfully", "data": new_item}


@router.get("/{item_id}", summary="Get an item by ID", description="Endpoint to retrieve an item by its ID.")
async def get_item_by_id_router(session: SessionDependency, item_id: int):
    # Роутеру не потрібно робити перевірку, він довіряє сервісу
    item = await get_item_by_id(session, item_id)
    
    return {"message": "Item retrieved successfully", "data": item}


@router.delete("/{item_id}", summary="Delete an item by ID", description="Endpoint to delete an item by its ID.")
async def delete_item_router(session: SessionDependency, item_id: int):
    success = await delete_item(session, item_id)
    if success:
        return {"message": "Item deleted successfully"}
    