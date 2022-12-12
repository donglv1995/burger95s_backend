
CREATE DATABASE burger95s;

CREATE TABLE user(
    user_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    gender VARCHAR(5) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    is_deleted BOOLEAN NOT NULL
);

ALTER TABLE USER_INFO ALTER COLUMN is_deleted SET DEFAULT FALSE;

INSERT INTO USER_INFO(user_name, gender, phone)  VALUES('KyQuan', 'M', 0909760520);
INSERT INTO USER_INFO(user_name, gender, phone) VALUES('DongLuong', 'M', 0123258987);
INSERT INTO USER_INFO(user_name, gender, phone)  VALUES('DuaEm', 'M', 090974456, 'true');
INSERT INTO USER_INFO(user_name, gender, phone)  VALUES('KyQuan', 'M', 0909795687);



CREATE TABLE item(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price BIGINT NOT NULL,
    type VARCHAR(50) NOT NULL,
    size VARCHAR(5),
    is_deleted BOOLEAN NOT NULL
);

ALTER TABLE item ALTER COLUMN is_deleted SET DEFAULT FALSE;

INSERT INTO item(name, price, description) 
VALUES('Beef', 45000,'burger'), 
('Beef', 55000,'burger'), ('Chicken', 38000,'burger'), 
('Sausage Bacon', 45000,'burger'), ('Sausage Egg', 35000,'burger'),
('Bacon Egg', 35000,'burger'), ('Shrimp', 50000,'burger'), ('Combo 2', 65000,'burger'),
('Combo 2', 60000,'burger'), ('Special', 60000,'burger'), ('Double Beef', 70000,'burger'),
('French Fires', 15000,'side dish'),
('French Fries Cheese Bacons', 28000, 'side dish'),
('Shake Potato', 20000, 'side dish'),
('Chicken Nugget', 30000, 'side dish'), ('Croissant', 12000, 'side dish'),
('Bacon', 15000, 'extra'), ('Beef', 20000, 'extra'), ('Egg', 5000, 'extra'),
('Chicken', 12000, 'extra'), ('Sausage', 12000, 'extra'), ('Cheese', 3500, 'extra');


INSERT INTO items(item_name, quantity) VALUES
1('burger white', 10),
('burger black', 10), 
3('beef', 10), ('chicken', 10), ('bacon', 10),
('fish', 20), ('shrimp', 10), 
8('salad', 50), ('onion', 50), ('tomato', 50),
('cucumber', 50), ('cheese', 50), 
13('french fires', 10), ('eggs', 20);

INSERT INTO product(product_name) VALUES('beef burger'), ('double beef burger'), ('chicken burger'),
('bacon burger'), ('bacon eggs burger'), ('fish burger'), ('shrimp burger');

INSERT INTO orders(consumer_name, product_id) VALUES ('Ky Quan', 5), ('Dong Luong', 2), ('Hiep', 6), ('Dua Em', 7);

INSERT INTO order_product_item(order_id,product_id, item_id,quantity) VALUES (1,3,1,1), (1,3,4,1), (1,3,8,1), (1,3,9,1), (1,3,10,1),(1,3,11,1),(1,3,12,1),
(1,5,2,1),(1,5,5,1),(1,5,14,1),(1,5,8,1),(1,5,9,1),(1,5,10,1),(1,5,11,1),(1,5,12,1),
(1,6,1,1),(1,6,6,2),(1,6,8,1),(1,6,9,1),(1,6,10,1),(1,6,12,1),
(2,2,2,1),(2,2,3,2),(2,2,8,1),(2,2,9,1),(2,2,12,2),
(2,3,1,1),(2,3,4,1),(2,3,9,2),(2,3,12,2),
(3,1,1,1),(3,1,3,1),(3,1,8,2),(3,1,11,2),(3,1,12,2),
(3,6,2,1),(3,6,6,1),(3,6,8,2),(3,6,12,1),
(4,2,1,1),(4,2,3,2),(4,2,8,2),(4,2,12,2),
(6,2,2,1),(6,2,3,2),(6,2,8,1),(6,2,9,1),(6,2,10,1),(6,2,12,1),
(6,4,2,1),(6,4,5,2),(6,4,8,1),(6,4,12,2);



"update value (array) for an specific column"
 UPDATE order_product op SET description = ARRAY(SELECT item_id FROM order_product_item WHERE order_id = 1 AND product_id = 6) 
 WHERE order_id = 1 AND product_id = 6;

 "get product_name by id"
 SELECT pro.product_name FROM product pro INNER JOIN order_product opr ON pro.product_id = opr.product_id 
 INNER JOIN orders ord ON ord.order_id = opr.order_id WHERE ord.order_id = o.order;
 
 "get orders"
 SELECT o.order_id, o.consumer_name, 
 ARRAY(SELECT pro.product_name FROM product pro INNER JOIN order_product opr ON pro.product_id = opr.product_id INNER JOIN orders ord ON ord.order_id = opr.order_id WHERE ord.order_id = o.order_id) 
 FROM orders o INNER JOIN order_product op ON o.order_id = op.order_id 
 INNER JOIN product p ON p.product_id = op.product_id GROUP BY o.order_id;