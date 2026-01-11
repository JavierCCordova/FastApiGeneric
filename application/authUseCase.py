
class LoginUseCase:
    
    def __init__(self, userRepo, hasher, tokenService):
        self.userRepo       =   userRepo    #Objeto de domain, que se declara en memoria.
        self.hasher         =   hasher  
        self.tokenService   =   tokenService
        
    async def execute(self, username: str, password: str):
        user    =   await self.userRepo.getByUserName(username)
        if not user or not self.hasher.verify(password,user.hashPassword):
            raise Exception("Credenciales invalidas")
        
        return self.tokenService.createAccessToken({'sub': user.userName})