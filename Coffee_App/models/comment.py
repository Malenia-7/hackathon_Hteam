from ..extensions import db

class Comment(db.Model):
    __tablename__ = 'Comments'

    id = db.Column(
        db.BigInteger,
        primary_key = True,
        nullable = False,
        autoincrement = True
    )

    user_id = db.Column(
        db.BigInteger,
        nullable = False
    )

    post_id = db.Column(
        db.BigInteger,
        nullable = False
    )

    content = db.Column(
        db.Text,
        nullable = False
    )

    created_at = db.Column(
        db.DateTime,
        server_default = db.func.current_timestamp(),
        nullable = False
    )

    updated_at = db.Column(
        db.DateTime,
        server_default = db.func.current_timestamp(),
        nullable = False
    ) 