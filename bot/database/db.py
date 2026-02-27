import psycopg2

from bot.config import settings


class DB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            user=settings.DB_USER,
            password=settings.DB_PASS,
            dbname=settings.DB_NAME,
        )
        self.cur = self.conn.cursor()

    def add_user(self, name, email):
        query = """
        INSERT INTO users (name, email)
        VALUES (%s, %s)
        RETURNING id
        """
        self.cur.execute(query, (name, email))
        self.conn.commit()

    def add_location(self, latitude, longitude):
        query = """
        INSERT INTO locations (latitude, longitude)
        VALUES (%s, %s)
        """
        self.cur.execute(query, (latitude, longitude))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


db = DB()
