-- Creates a table users with atttributes:
-- id, integer NOTNULL, AUTO_INCREMENT, PRIMARYKEY
-- email, VARCHAR(255) NOTNULL, UNIQUE
-- name, VARCHAR(255) NOTNULL
-- country, enumeration: US, CO and TN NOT NULL
-- default will be first element of enumeration

-- Create "users" table.
CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL,
	UNIQUE (email),
	PRIMARY KEY (id)
	);
