from flask import Flask
from sqlalchemy import text

from Coffee_App.config import Config
from Coffee_App.extensions import db


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    @app.route("/")
    def index():
        return "Coffee App is running!"

    @app.route("/db-test")
    def db_test():
        try:
            db.session.execute(text("SELECT 1"))
            return "Database connection successful!"
        except Exception as e:
            return f"Database connection failed: {e}", 500

    return app