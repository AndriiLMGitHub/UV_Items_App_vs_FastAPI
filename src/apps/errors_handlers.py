# error_handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse
from apps.exceptions import ItemNotFoundError

async def item_not_found_exception_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "detail": {
                "message": str(exc),
                "data": None
            }
        }
    )