import pytest
import time
import os
import redis
from app import app
from database import db

@pytest.fixture(scope="session", autouse=True)
def wait_for_services():
    """Waiting for MySQL and Redis awake"""
    retries = 10
    db_ready = False
    while retries > 0:
        try:
            with db.get_cursor(db.root_user, db.root_password) as cursor:
                cursor.execute("SELECT 1")
                db_ready = True
                break
        except Exception:
            retries -= 1
            time.sleep(2)

    if not db_ready:
        pytest.exit("MySQL is not responding. Check docker logs.")

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

