from pydantic import BaseModel
from pydantic import EmailStr


class UserBase(BaseModel):
   email: EmailStr


class UserCreate(UserBase):
   last_name: str
   first_name: str
   password: str