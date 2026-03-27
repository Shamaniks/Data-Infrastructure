import os
from pymongo import MongoClient

class MongoDatabase:
    def __init__(self):
        self.uri = os.getenv(
            "MONGO_URI",
            "mongodb://root:root_password@mongo:27017/shopdb?authSource=admin"
        )
        self._client = None

    def get_client(self):
        """Returns pymongo client"""
        if self._client is None:
            self._client = MongoClient(self.uri)
        return self._client

    def get_collection(self, collection_name: str = "products"):
        """Returns a collection"""
        client = self.get_client()
        db = client["shopdb"]
        return db[collection_name]

# Global instance
mongo_db = MongoDatabase()
