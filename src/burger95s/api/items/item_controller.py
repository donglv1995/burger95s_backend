from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "NOT Found"}},
)

@router.get("/") # items/
async def get_items():
    return [
    ]

@router.get("/{itemid}") # /items/{itemid}
async def get_item(itemid: int):
    return {}