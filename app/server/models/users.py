from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    fullname: str 
    email: EmailStr 
    country: str 
    date: date 
    cell_phone: str 

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'John Doe',
                'email': 'john@example.com',
                'country':  'United States',
                'date': '1999-01-13',
                'cell_phone':   '(185)-561-7071',
            }
        }

class UpdateUserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[str]
    country: Optional[EmailStr]
    date: Optional[date] 
    cell_phone: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'John Doe',
                'email': 'john@example.com',
                'country':  'United States',
                'date': '1999-01-13',
                'cell_phone':   '(185)-561-7071',
            }
        }

def response_model(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message,
    }

def error_response_model(error, code, message):
    return {'error': error, 'code': code, 'message': message}
