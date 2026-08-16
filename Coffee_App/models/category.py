from ..extensions import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.BigInteger, primary_key=True, nullable=False, autoincrement=True)

    category_name = db.Column(db.String(50), nullable=False, unique=True)

    created_at = db.Column(
        db.DateTime, server_default=db.func.current_timestamp(), nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
        nullable=False,
    )
