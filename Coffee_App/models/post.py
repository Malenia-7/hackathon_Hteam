def insert_post(cursor, user_id, content):
    sql = """
        INSERT INTO posts (
            user_id,
            content,
            visibility
        )
        VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (user_id, content, "public"))
    return cursor.lastrowid


def find_post_by_id(cursor, post_id):
    sql = """
        SELECT
            id,
            user_id,
            content,
            visibility,
            created_at,
            updated_at
        FROM posts
        WHERE id = %s
          AND deleted_at IS NULL
    """
    cursor.execute(sql, (post_id,))
    return cursor.fetchone()


def find_posts(cursor):
    cursor.execute(
        """
        SELECT
            id,
            user_id,
            content,
            visibility,
            created_at,
            updated_at
        FROM posts
        WHERE deleted_at IS NULL
          AND visibility = 'public'
        ORDER BY created_at DESC, id DESC
        LIMIT 100
        """
    )
    return cursor.fetchall()


def delete_post(cursor, post_id):
    cursor.execute(
        "UPDATE posts SET deleted_at = CURRENT_TIMESTAMP(6) WHERE id = %s",
        (post_id,),
    )
