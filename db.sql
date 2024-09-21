-- prepares a MySQL server for the project
DROP DATABASE IF EXISTS lt_store;
CREATE DATABASE IF NOT EXISTS lt_store;
CREATE USER IF NOT EXISTS 'ziad4036'@'localhost' IDENTIFIED BY 'ltstore';
GRANT ALL PRIVILEGES ON `lt_store`.* TO 'ziad4036'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'ziad4036'@'localhost';
FLUSH PRIVILEGES;
