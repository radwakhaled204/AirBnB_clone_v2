-- Create or use the hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create or use the hbnb_dev user with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Display the current grants for hbnb_dev user
SHOW GRANTS FOR 'hbnb_dev'@'localhost';
