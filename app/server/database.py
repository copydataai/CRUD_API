import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = 'mongodb://localhost:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

users_collection = database.get_collection('users_collection')

# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in users_collection.find():
        users.append(users_helper(user))
    return users

# Add a new student into to the database
async def add_user(user_data: dict) -> dict:
    user = await users_collection.insert_one(user_data)
    new_user = await users_collection.find_one({'_id': user.inserted_id})
    return users_helper(new_user)

# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await users_collection.find_one({'_id': ObjectId(id)})
    if user:
        return users_helper(user)

#Update a users with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await users_collection.find_one({'_id': ObjectId(id)})
    if user:
        updated_student = await users_collection.update_one(
            {'_id': ObjectId(id)}, {'$set': data}
        )
        if updated_student:
            return True
        return False



# Delete a user from the database
async def delete_user(id: str):
    user = await users_collection.find_one({'_id': ObjectId(id)})
    if user:
        await users_collection.delete_one({'_id': ObjectId(id)})
        return True


def users_helper(users) -> dict:
    return{
        'id': str(users['_id']),
        'fullname': users['fullname'],
        'email': users['email'],
        'country': users['country'],
        'date': users['date'],
        'cellphone': users['cellphone'],
    }

