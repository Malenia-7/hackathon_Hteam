import os
from pathlib import Path


class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "db")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_CHARSET = "utf8mb4"

    # TODO: 認証機能の統合後、ログイン中のユーザーIDに置き換えて削除する。
    DEV_USER_ID = int(os.getenv("DEV_USER_ID", "1"))

    # アップロード画像の保存先
    POST_UPLOAD_FOLDER = str(
        Path(__file__).resolve().parent / "static" / "uploads" / "posts"
    )
    ALLOWED_IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
