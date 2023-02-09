-- CREATES a table users with:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)

-- Create "users" table
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL,
	name VARCHAR(255),
	UNIQUE (email),
	PRIMARY KEY (id)
	);
