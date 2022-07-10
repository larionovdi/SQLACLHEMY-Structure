from fastapi import APIRouter
from starlette.responses import JSONResponse
import typing

from containers import Container
from users.services import list_users, get_user_by_id, create_user, update_user_balance
from users.api.schemas import UserCreateSchema, UserUpdateSchema

class CustomResponse(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        return super(CustomResponse, self).render({
            "data": content,
            "version": "1.0.0"
        })


router = APIRouter(default_response_class=CustomResponse)



@router.get('/')
async def list_users_route():
    return list_users()

@router.get('/{id}')
async def get_user_route(id: int):
    return get_user_by_id(id=id)

@router.post('/')
async def create_user_route(user_create:UserCreateSchema):
    create_user(user_create.username) 
    return {"ack": True}

@router.patch('/update_balance/{id}')
async def update_user_balance_route(id:int, user_update:UserUpdateSchema):
    update_user_balance(id=id, balance_change = user_update.balance_change)
    return {"ack": True}