from jose import jwt
from datetime import datetime, timedelta, timezone
from  core.config import Settings

class TokenService:
    
    def __init__(self,settings: Settings):
        self.settings   =   settings
        
        
    def createAccessToken(self, data: dict):
        payload         =   data.copy()
        payload['exp']  =   datetime.now(timezone.utc) + timedelta(minutes=self.settings.ACCESS_TOKEN_EXPIRE_MINUTES)   
        return jwt.encode(payload, self.settings.SECRET_KEY, algorithm= "HS256")
    
            