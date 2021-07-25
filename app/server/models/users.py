from typing import Optional
from pydantic import BaseModel, EmailStr, Field
import datetime

class UserSchema(BaseModel):
    fullname: str = Field(..., max_length=100)
    email: EmailStr = Field(...)
    country: str = Field(...) 
    date: datetime.date = Field(...) 
    cellphone: str = Field(...) 

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'John Doe',
                'email': 'john@example.com',
                'country':  'United States',
                'date': '1999-01-13',
                'cellphone':'(185)-561-7071',
            }
        }

class UpdateUserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    country: Optional[str]
    date: Optional[str] 
    cellphone: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'John Doe',
                'email': 'john@example.com',
                'country':  'United States',
                'date': '1999-01-13',
                'cellphone':'(185)-561-7071',
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
