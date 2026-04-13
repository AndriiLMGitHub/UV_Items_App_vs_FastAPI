from fastapi import APIRouter, Depends
from typing import Annotated

from apps.user.schemas import UserCreate, UserItemResponse, UsersListResponse
from apps.user.services import create_user_service, get_all_users_service
from database.dependencies import SessionDependency

router = APIRouter(
    prefix="/api/users",
    tags=["API Users Endpoints"]
)

@router.get("/", summary="Get all users", description="Endpoint to retrieve all users.")
async def get_all_users_router(session: SessionDependency):
    users = await get_all_users_service(session)
    # Зверни увагу: ми пакуємо список users у поле data
    return {"message": "Users retrieved successfully", "data": users}


@router.post("/", summary="Create a user", description="Endpoint to create a new user.")
async def create_user_router(session: SessionDependency, user_data: Annotated[UserCreate, Depends()]):
    new_user = await create_user_service(session, user_data)
    return {"message": "User created successfully", "data": new_user}