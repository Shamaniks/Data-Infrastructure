import hashlib
import json

import connectors

def store_session(login: str, token: str, ttl_hours: int = 12):
    """Save JWT in Redis for revocation and fast validation"""
    redis = connectors.get_redis()
    ttl_seconds = ttl_hours * 3600
    
    # Main session key
    redis.setex(f"auth:session:{login}", ttl_seconds, token)
    
    # Token hash blacklist support
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    redis.setex(f"auth:token:{token_hash}", ttl_seconds, login)

def invalidate_session(login: str):
    """Logout – instant revocation"""
    redis = connectors.get_redis()
    token = redis.get(f"auth:session:{login}")
    if token:
        token_hash = hashlib.sha256(token.encode()).hexdigest()
        redis.delete(f"auth:token:{token_hash}")
    redis.delete(f"auth:session:{login}")

def is_token_valid(login: str, token: str) -> bool:
    """Check if token is still valid in Redis"""
    redis = connectors.get_redis()
    stored = redis.get(f"auth:session:{login}")
    return stored == token

