from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_user,
    delete_user, 
    update_user, 
    retrieve_user, 
    retrieve_users)

from app.server.models.users import (
    error_response_model, 
    response_model,
    UserSchema,
    UpdateUserModel)

router = APIRouter()


@router.post('/', response_description='User data added into the database')
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return response_model(new_user, "User added successfully.")


@router.delete('/{id}', response_description='User data deleted from the database')
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return response_model(
            f'User with ID: {id} removed',
            'User deleted successfully'
        )
    return error_response_model(
        'An error occurred', 
        404,
        f'User with id {id} doesnt\' exist'
    )



@router.get('/', response_description='Users retrieved.')
async def get_users():
    users = await retrieve_users()
    if users:
        return response_model(users, 'Users data retrieved successfully.')
    return response_model(users, 'Empty list returned')

@router.get('/{id}', response_description='User data retrieved')
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return response_model(user, 'User data retrieved successfully')
    return error_response_model('An error occurred.', 404, 'User doesn\'t exist.')


@router.put('/{id}')
async def update_user_data(id: str, req: UpdateUserModel):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return response_model(
            f'User with ID: {id} name update is successful',
            'User name updated successfully'
        )
    return error_response_model(
        'An error occurred', 
        404,
        'There was an error updating the user data.',
    )
