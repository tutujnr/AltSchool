
CREATE DATABASE IF NOT EXISTS secure_auth_db;
USE secure_auth_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(64) NOT NULL,
    role VARCHAR(20) NOT NULL
);

INSERT INTO users (username, password_hash, role)
VALUES ('admin', SHA2('admin123', 256), 'admin');

