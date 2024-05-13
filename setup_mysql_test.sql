-- Create or use the hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or use the hbnb_test user with password hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Display the current grants for hbnb_test user
SHOW GRANTS FOR 'hbnb_test'@'localhost';
