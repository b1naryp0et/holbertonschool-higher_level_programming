-- Script which creates table on server
CREATE table IF NOT EXISTS unique_id(id INT default 1 UNIQUE, name VARCHAR(256));
