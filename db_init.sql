
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
('Bacon Egg', 35000,'burger'), ('Shrimp', 50000,'burger'), ('Combo 1', 65000,'burger'),
('Combo 2', 60000,'burger'), ('Special', 60000,'burger'), ('Double Beef', 70000,'burger'),
('French Fires', 15000,'side dish'),
('French Fries Cheese Bacons', 28000, 'side dish'),
('Shake Potato', 20000, 'side dish'),
('Chicken Nugget', 30000, 'side dish'), ('Croissant', 12000, 'side dish'),
('Bacon', 15000, 'extra'), ('Beef', 20000, 'extra'), ('Egg', 5000, 'extra'),
('Chicken', 12000, 'extra'), ('Sausage', 12000, 'extra'), ('Cheese', 3500, 'extra');


