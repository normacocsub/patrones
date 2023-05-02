from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.responses import JSONResponse
from ..services import retry, circuit
from app.schemas import UserCreate, UserBase, User
router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_method(data: dict = Body(...)):
    try:
        user_create = UserCreate(**data)

        response = await retry.post_data_with_retry("http://localhost:8001/users/", user_create)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error: " + str(e),
        )

@router.post("/prueba", status_code=status.HTTP_201_CREATED)
def post_method(data: dict = Body(...)):
    try:
        user_create = UserCreate(**data)

        response = circuit.make_request("http://localhost:8001/users/", user_create)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error: " + str(e),
        )


