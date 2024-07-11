CREATE DATABASE IF NOT EXISTS mock_database;

USE mock_database;

CREATE TABLE IF NOT EXISTS top_scorers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    goals INT NOT NULL
);

INSERT INTO top_scorers (country, goals) VALUES
('Italy', 13),
('Spain', 13),
('England', 11),
('Denmark', 12),
('Switzerland', 9);

