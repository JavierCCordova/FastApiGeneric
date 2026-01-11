from fastapi import APIRouter, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer 
from api.dependencies import getLoginUseCase
router  =   APIRouter(prefix= "/auth")

@router.post("login")
async def loginUser(form: OAuth2AuthorizationCodeBearer = Depends(), usecase = Depends(getLoginUseCase)):
    token   =   await usecase.execute(form.username, form.password)
    return { "accessToken": token }