import pymysql
import os
from contextlib import contextmanager

class Database:
    def __init__(self):
        self.config = {
            "host": os.getenv('DB_HOST', 'db'),
            "user": os.getenv('DB_USER', 'root'),
            "password": os.getenv('DB_PASSWORD', 'root_password'),
            "database": os.getenv('DB_NAME', 'data_infrastructure'),
            "cursorclass": pymysql.cursors.DictCursor,
            "charset": 'utf8mb4',
            "use_unicode": True
        }

    @contextmanager
    def get_cursor(self):
        conn = pymysql.connect(**self.config)
        try:
            with conn.cursor() as cur:
                yield cur
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

db = Database()

