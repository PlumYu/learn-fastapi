from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/list")
async def user_list():
    return {"users":['zs','ls']}

@router.get("/{user_id}")
async def user_details(user_id: int):
    return {"user_id":user_id}