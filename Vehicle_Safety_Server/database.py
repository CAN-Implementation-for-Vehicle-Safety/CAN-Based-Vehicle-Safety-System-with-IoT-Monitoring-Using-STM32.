import mysql.connector
from config import *

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


def insert_data(distance, temperature, gas, rain):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO vehicle_data
        (distance, temperature, gas, rain)
        VALUES (%s, %s, %s, %s)
        """

        values = (distance, temperature, gas, rain)

        cursor.execute(sql, values)
        conn.commit()

        print("Data Inserted Successfully")

    except Exception as e:
        print("Database Error :", e)

    finally:
        cursor.close()
        conn.close()