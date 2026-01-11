
from domain.user.ports import UserRepositoryPort
from domain.user.entities   import UserEntity

class MongoRepository(UserRepositoryPort):
    
    def __init__(self, session):
        self.session    =   session
        
    async def getbyUsername(self, username: str)->UserEntity | None:
        
        userCollection  =   self.collection.find_one({'username':username})
        if not userCollection:
            return None
         
        return UserEntity(
            id          =   str(userCollection['id']),
            userName    =   userCollection['username'] ,
            hashPassword=   userCollection['password'] 
        )
        