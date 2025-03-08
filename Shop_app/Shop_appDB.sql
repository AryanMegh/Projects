create database Shop_appDB;
use Shop_appDB;

 CREATE TABLE Admin_login( 
    Admin_Userid INT AUTO_INCREMENT PRIMARY KEY, 
    Admin_name VARCHAR(100), 
    Admin_Username VARCHAR(100), 
    Admin_Email VARCHAR(100), 
    Admin_Password VARCHAR(100) 
);

INSERT INTO Admin_login(Admin_name,Admin_Username,Admin_email,Admin_password) VALUES("Aryan Meghraj Shivgunde","Aryan","aryanshivgunde@gmail.com","Aryan@2025");

CREATE TABLE User_credential(
    User_name VARCHAR(100),
    User_lastname VARCHAR(100),
    User_username VARCHAR(100),
    User_email VARCHAR(100),
    User_password VARCHAR(100),
    User_confirmpassword VARCHAR(100)
);

SELECT * FROM User_credential;

CREATE TABLE Login(
    User_email VARCHAR(100),
    User_password VARCHAR(100)
);

CREATE TABLE Product (
    Prod_id INT AUTO_INCREMENT PRIMARY KEY,
    Prod_name VARCHAR(100),
    Prod_quantity INT,
    Prod_price DECIMAL(10, 2)
);

insert INTO  Product(Prod_name,Prod_quantity,Prod_price) VALUES('DellG15 Laptop',1,90000.00);
insert INTO  Product(Prod_name,Prod_quantity,Prod_price) VALUES('Smartphone', 20, 600.00);
insert INTO  Product(Prod_name,Prod_quantity,Prod_price) VALUES('Headphones', 30, 50.00);
insert INTO  Product(Prod_name,Prod_quantity,Prod_price) VALUES('Smartwatch', 15, 150.00);
insert INTO  Product(Prod_name,Prod_quantity,Prod_price) VALUES('Tablet', 12, 300.00);

SELECT * FROM Product;

Create table Order_detail(
	Order_id INT AUTO_INCREMENT PRIMARY KEY,
    User_id INT,
    Prod_id INT,
    Quantity INT,
    Total_price decimal(10,2),
    foreign key(User_id)  references User_login(User_id),
    foreign key(Prod_id) references Product(Prod_id)
);