from motor.motor_asyncio import AsyncIOMotorClient

def getMongo():
    client  =   AsyncIOMotorClient("mongodb://localhost:27017")
    return client["mydb"]["users"]