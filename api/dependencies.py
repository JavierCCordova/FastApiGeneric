from fastapi import Depends
from application.authUseCase import LoginUseCase
from infrastructure.security.hasher import PasswordHasher
from infrastructure.security.tokenService import TokenService
from core.config import getSettings
from infrastructure.persistence.mongodb.connection import getMongo
from infrastructure.persistence.mongodb.userRepository import MongoRepository


async def getUserRepository():
    collection  =   getMongo()
    return MongoRepository(collection)

async def getLoginUseCase(settings = Depends(getSettings)):
    
    repo    =  await getUserRepository()
    
    return LoginUseCase(
        userRepo=       repo,
        hasher=         PasswordHasher(),
        tokenService=   TokenService(settings)
    )