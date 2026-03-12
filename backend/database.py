import pymysql
import os
from contextlib import contextmanager

class Database:
    def __init__(self):
        self.host = os.getenv('DB_HOST', 'db')
        self.database = os.getenv('DB_NAME', 'data_infrastructure')
        self.cursorclass = pymysql.cursors.DictCursor
        self.charset = 'utf8mb4'
        self.use_unicode = True

        self.root_user = os.getenv('DB_USER', 'root')
        self.root_password = os.getenv('DB_PASSWORD', 'root_password')

    @contextmanager
    def get_cursor(self, db_user="client", db_pass="Pa$$w0rd"):
        """Connects to MySQL as a specific database user role."""
        connection = pymysql.connect(
            host=self.host,
            user=db_user,
            password=db_pass,
            database=self.database,
            cursorclass=self.cursorclass,
            charset=self.charset,
            use_unicode=self.use_unicode
        )
        try:
            with connection.cursor() as cursor:
                yield cursor
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

db = Database()

