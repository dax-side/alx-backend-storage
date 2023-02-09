-- Creates a Trigger that decreases the quantity on an item after adding a new order
CREATE TRIGGER decrase_quantITY AFTER insert
ON orders FOR each ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE NEW.item_name = name; 
