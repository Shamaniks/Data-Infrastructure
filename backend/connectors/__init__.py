# connectors/__init__.py
from .mysql import db
from .redis import redis_client
from .mongo import mongo_db

def get_mysql():
    """Returns MySQL instance"""
    return db

def get_redis():
    """Returns Redis client instance"""
    return redis_client

def get_mongo():
    """Returns MongoDB instance"""
    return mongo_db
