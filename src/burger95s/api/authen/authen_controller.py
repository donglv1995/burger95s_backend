from fastapi import APIRouter

router = APIRouter(
    prefix="/authentication",
    tags=["authentication"]
)

@router.get("/")
async def validate_user():
    return True