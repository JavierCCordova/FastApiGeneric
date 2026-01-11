from pydantic import BaseModel
from typing import Protocol, Optional

class userEntity(BaseModel):
    
    id:             int
    userName:       str
    hashPassword:   str
    
    
class UserRepositoryPort(Protocol):
    async def getByUserName(self, userName: str) ->Optional[userEntity]:
        ...
        #return userEntity(id=1, userName="Holamundo",hashPassword="holamundo2")
    