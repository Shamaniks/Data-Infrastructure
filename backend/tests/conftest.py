import pytest
import time
import os
import redis
from app import app
from database import get_db_connection

@pytest.fixture(scope="session", autouse=True)
def wait_for_services():
    """Waiting for MySQL and Redis awake"""
    db_ok = False
    for _ in range(10):
        try:
            conn = get_db_connection()
            conn.close()
            db_ok = True
            break
        except Exception:
            time.sleep(2)
    
    if not db_ok:
        pytest.exit("MySQL is down. Stopping.")

    try:
        r = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379)
        r.ping()
    except Exception:
        print("Warning: Redis is not reachable, some tests might fail.")

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def redis_conn():
    return redis.Redis(
        host=os.getenv('REDIS_HOST', 'redis'), 
        port=6379, 
        decode_responses=True
    )

