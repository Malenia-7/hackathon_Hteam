import os
from pathlib import Path


class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://"
        f"{os.getenv('MYSQL_USER')}:"
        f"{os.getenv('MYSQL_PASSWORD')}@"
        f"db:3306/"
        f"{os.getenv('MYSQL_DATABASE')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False