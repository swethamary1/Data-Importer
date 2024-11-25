import psycopg2
from psycopg2.extras import Json
from data_importer.logger import get_logger

logger = get_logger(__name__)

class Database:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        try:
            conn = psycopg2.connect(**self.db_config)
            return conn
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise

    def insert_phone_data(self, phone_id, phone_name, phone_data):
        query = """
        INSERT INTO public.phone (phoneid, phone_name, phone_data)
        VALUES (%s, %s, %s)
        ON CONFLICT (phoneid) DO NOTHING;
        """
        conn = self.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(query, (phone_id, phone_name, Json(phone_data)))
            conn.commit()
        except Exception as e:
            logger.error(f"Error inserting data: {e}")
        finally:
            conn.close()
