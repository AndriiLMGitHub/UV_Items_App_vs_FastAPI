from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.items.errors_handlers import item_not_found_exception_handler
from apps.items.exceptions import ItemNotFoundError
from apps.items.routes import router as items_router
from apps.user.routes import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    print("Starting up the application...")
    yield
    # Code to run on shutdown
    print("Shutting down the application...")


app = FastAPI(\
    title="My FastAPI Application",
    description="This is a sample FastAPI application with lifespan events.",
    version="1.0.0",
    lifespan=lifespan
    )

# Реєстрація глобальних обробників помилок
app.add_exception_handler(ItemNotFoundError, item_not_found_exception_handler)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users_router)
app.include_router(items_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)