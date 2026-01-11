from pydantic import BaseModel

class UserEntity(BaseModel):
    
    id:             int
    userName:       str
    hashPassword:   str