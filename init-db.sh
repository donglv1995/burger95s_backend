#!/bin/bash
set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $APP_DB_USER;
  CREATE DATABASE $APP_DB_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $APP_DB_NAME TO $APP_DB_USER;

    BEGIN;
        CREATE TABLE IF NOT EXISTS User (
            user_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            user_name VARCHAR(50) NOT NULL,
            gender VARCHAR(5) NOT NULL,
            phone VARCHAR(50),
            is_deleted BOOLEAN DEFAULT False
        );
    INSERT INTO User VALUES('KyQuan', 'M', 0909760520);
    INSERT INTO User VALUES('DongLuong', 'M', '1234567890', True);
    INSERT INTO User VALUES ('DuaEm', 'M', null);
    COMMIT;
EOSQL