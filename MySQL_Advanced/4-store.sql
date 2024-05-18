-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER trigger
    AFTER INSERT
    ON orders FOR
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE NEW.item_name = name;