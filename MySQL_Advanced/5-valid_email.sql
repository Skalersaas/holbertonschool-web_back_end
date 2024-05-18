-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

CREATE TRIGGER CHECK_EMAIL
    AFTER UPDATE ON users
    FOR EACH ROW
    WHERE email <> NEW.email
    SET valid_email = 0;
