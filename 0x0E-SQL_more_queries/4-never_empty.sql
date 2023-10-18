-- id but not null
CREATE TABLE id_not_null (id INT DEFAULT 1, name VARCHAR(256), UNIQUE (id));