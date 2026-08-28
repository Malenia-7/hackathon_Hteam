import os
import pymysql


def get_db_connection():
    return pymysql.connect(
        host="db",
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
        charset="utf8mb4"
    )
