-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

CREATE TRIGGER CHECK_EMAIL
    AFTER INSERT ON users
    FOR EACH ROW
    valid_email = email REGEXP "^[a-zA-Z0-9][a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$"
