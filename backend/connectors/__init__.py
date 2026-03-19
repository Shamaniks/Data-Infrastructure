from .mysql import db
from .redis import redis_client

def get_mysql(): 
    """Returns MySQL instance"""
    return db

def get_redis(): 
    """Returns Redis client instance"""
    return redis_client
