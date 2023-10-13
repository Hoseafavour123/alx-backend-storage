-- A trigger that decreases the quantity of an item after an order is made
CREATE TRIGGER decrement
AFTER INSERT ON orders
FOR EACH ROW
	UPDATE items SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name
