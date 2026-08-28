SET NAMES utf8mb4;

CREATE TABLE categories(
    id BIGINT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
    updated_at TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
);

-- カテゴリー初期データ
INSERT INTO categories (category_name) VALUES
('コーヒーレシピ'),
('今日のコーヒー'),
('道具'),
('お店レビュー'),
('おやつ・お供'),
('その他');