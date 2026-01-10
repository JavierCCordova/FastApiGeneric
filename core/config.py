from functools import lru_cache ##revisar a fondo
from  pydantic_settings import BaseSettings ##revisar a fondo


class Settings(BaseSettings):
    SECRET_KEY  :   str
    ACCESS_TOKEN_EXPIRE_MINUTES :   int=30
    
    class Config:
        env_file    =   ".env"
        
        
@lru_cache
def getSettings():
    return Settings()

# BaseSettings lee automáticamente .env
# lru_cache() evita que se lea el archivo cada vez.