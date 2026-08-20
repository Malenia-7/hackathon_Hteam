# コメント一覧の取得
SELECT * FROM comments  WHERE post_id=%s;

# コメントの削除
DELETE FROM comments WHERE post_id=%s;

# コメントの投稿
INSERT INTO comments (content, user_id, post_id) VALUES (%s, %s, %s);
