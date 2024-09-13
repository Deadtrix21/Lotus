import motor.motor_asyncio


class MongoDBFactory:
    def __init__(self, mongo_uri: str):
        self.mongo_client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)

    def get_client(self):
        return self.mongo_client
