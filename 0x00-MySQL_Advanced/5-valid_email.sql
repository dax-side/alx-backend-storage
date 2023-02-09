-- Creates a trigger that resets the attribute valid_email only when
-- the email has been changed
delimiter $$
CREATE TRIGGER email_valid 
BEFORE UPDATE ON users
FOR each ROW 
BEGIN 
    if NEW.email <> OLD.email 
    THEN SET NEW.valid_email = 0;
    end if;
END $$ 
delimiter ;
