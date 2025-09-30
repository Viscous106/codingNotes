CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    email TEXT,
    age INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, username)
VALUES ('Rajnish', 'bkl_rajnish');      

SELECT * FROM users;