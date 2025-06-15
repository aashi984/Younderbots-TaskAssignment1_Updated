CREATE DATABASE IF NOT EXISTS vaccination_data;

USE vaccination_data;

CREATE TABLE IF NOT EXISTS vaccinations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    vaccine_name VARCHAR(50) NOT NULL,
    dose_number INT NOT NULL,
    vaccination_date VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    contact_number VARCHAR(20) NOT NULL
);
