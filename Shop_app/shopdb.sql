CREATE DATABASE shop;

USE shop;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address TEXT,
    password VARCHAR(50),
    role ENUM('user', 'admin') DEFAULT 'user'
);

CREATE TABLE products (
    prod_id INT AUTO_INCREMENT PRIMARY KEY,
    prod_name VARCHAR(100),
    prod_quantity INT,
    price DECIMAL(10, 2)
);


CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    prod_id INT,
    quantity INT,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (prod_id) REFERENCES products(prod_id)
);

INSERT INTO products (prod_name, prod_quantity, price) VALUES
('Laptop', 10, 800.00),
('Smartphone', 20, 600.00),
('Headphones', 30, 50.00),
('Smartwatch', 15, 150.00),
('Tablet', 12, 300.00),
('Bluetooth Speaker', 25, 70.00);