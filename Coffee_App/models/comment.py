# コメント一覧の取得
SELECT * comments  WHERE post_id=%s;

# コメントの削除
DELETE FROM comments WHERE post_id=%s;

# コメントの追加
INSERT INTO comments (content, user_id, post_id) VALUES (%s, %s, %s);
