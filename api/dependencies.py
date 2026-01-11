from fastapi import Depends
from application.authUseCase import LoginUseCase
from infrastructure.security.hasher import PasswordHasher
from infrastructure.security.tokenService import TokenService
from core.config import getSettings

def getLoginUseCase(settings = Depends(getSettings)):
    return LoginUseCase(
        userRepo=       None,
        hasher=         PasswordHasher(),
        tokenService=   TokenService(settings)
    )
