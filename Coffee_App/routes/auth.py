from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash

from Coffee_App.models.user import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/auth-test")
def auth_test():
    return "Auth route is working!"


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # 必須項目チェック
    if not username or not email or not password:
        return {
            "message": "username, email, password are required"
        }, 400

    try:
        # メールアドレスの重複チェック
        existing_user = User.find_by_email(email)

        if existing_user:
            return {
                "message": "This email is already registered."
            }, 409

        # パスワードをハッシュ化
        password_hash = generate_password_hash(password)

        # ユーザー登録
        User.create(
            username,
            email,
            password_hash
        )

        return {
            "message": "User registered successfully!"
        }, 201

    except Exception as e:
        return {
            "message": f"User registration failed: {e}"
        }, 500

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    # 必須項目チェック
    if not email or not password:
        return {
            "message": "email and password are required."
        }, 400

    try:
        # メールアドレスからユーザーを検索
        user = User.find_by_email(email)

        # ユーザーが存在しない
        if not user:
            return {
                "message": "Invalid email or password."
            }, 401

        # パスワードが一致しない
        if not check_password_hash(
            user["password_hash"],
            password
        ):
            return {
                "message": "Invalid email or password."
            }, 401

        # ログイン成功
        return {
            "message": "Login successful!",
            "user_id": user["id"],
            "username": user["username"]
        }, 200

    except Exception as e:
        return {
            "message": f"Login failed: {e}"
        }, 500