from Coffee_App.models.database import get_db_connection


# コメント一覧の取得
def get_comments(post_id):
    conn = get_db_connection()
    cr = conn.cursor()

    sql = """SELECT * FROM comments  WHERE post_id=%s;"""
    cr.execute(sql, (post_id,))
    comments = cr.fetchall()

    cr.close()
    conn.close()
    return comments


# コメントの削除
def delete_comments(comment_id):
    conn = get_db_connection()
    cr = conn.cursor()

    sql = """DELETE FROM comments WHERE id=%s;"""
    cr.execute(sql, (comment_id,))
    conn.commit()

    cr.close()
    conn.close()


# コメントの投稿
def post_comments(content, user_id, post_id):
    conn = get_db_connection()
    cr = conn.cursor()

    sql = """INSERT INTO comments (content, user_id, post_id) VALUES (%s, %s, %s);"""
    cr.execute(sql, (content, user_id, post_id))
    conn.commit()

    cr.close()
    conn.close()
