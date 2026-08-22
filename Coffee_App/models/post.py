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
