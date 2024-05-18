-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

CREATE TRIGGER change_email
    BEFORE UPDATE ON users
    FOR EACH ROW
    WHERE NEW.email <> email
    SET NEW.valid_email = 0;
