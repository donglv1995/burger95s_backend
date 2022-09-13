
CREATE DATABASE burger95s;

CREATE TABLE USER_INFO(
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




