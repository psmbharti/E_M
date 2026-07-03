# Create Database

DROP DATABASE IF EXISTS manufacturing_supplychain;

CREATE DATABASE manufacturing_supplychain;

USE manufacturing_supplychain;

# Create Suppliers Table

CREATE TABLE Suppliers (

    Supplier_ID VARCHAR(10) PRIMARY KEY,

    Supplier_Name VARCHAR(150),

    Country VARCHAR(50),

    Category VARCHAR(100),

    Lead_Time_Days INT,

    Supplier_Rating DECIMAL(3,1)

);

# Create Purchase Orders Table
CREATE TABLE Purchase_Orders (

    PO_Number VARCHAR(15) PRIMARY KEY,

    Supplier_ID VARCHAR(10),

    Material VARCHAR(100),

    Order_Date DATE,

    Expected_Delivery DATE,

    Quantity INT,

    Unit_Price DECIMAL(10,2),

    PO_Amount DECIMAL(12,2),

    Status VARCHAR(30),

    FOREIGN KEY (Supplier_ID)

    REFERENCES Suppliers(Supplier_ID)

);

# Create Invoices Table
CREATE TABLE Invoices (

    Invoice_ID VARCHAR(15) PRIMARY KEY,

    PO_Number VARCHAR(15),

    Invoice_Date DATE,

    Invoice_Amount DECIMAL(12,2),

    Tax DECIMAL(10,2),

    Discount DECIMAL(10,2),

    Final_Amount DECIMAL(12,2),

    Calculated_Total DECIMAL(12,2),

    Invoice_Discrepancy BOOLEAN,

    Payment_Status VARCHAR(30),

    FOREIGN KEY (PO_Number)

    REFERENCES Purchase_Orders(PO_Number)

);

# Create Inventory Table
CREATE TABLE Inventory (

    Item_ID VARCHAR(15) PRIMARY KEY,

    Material VARCHAR(100),

    Warehouse VARCHAR(100),

    Stock INT,

    Reorder_Level INT,

    Inventory_Value DECIMAL(12,2),

    Low_Stock BOOLEAN

);

# Create Shipments Table
CREATE TABLE Shipments (

    Shipment_ID VARCHAR(15) PRIMARY KEY,

    PO_Number VARCHAR(15),

    Dispatch_Date DATE,

    Delivery_Date DATE,

    Delay_Days INT,

    Shipment_Status VARCHAR(30),

    FOREIGN KEY (PO_Number)

    REFERENCES Purchase_Orders(PO_Number)

);

# Verify Tables
SHOW TABLES;

# Verify Table Structure
DESCRIBE Suppliers;

DESCRIBE Purchase_Orders;

DESCRIBE Invoices;

DESCRIBE Inventory;

DESCRIBE Shipments;

# Load Suppliers
LOAD DATA INFILE
'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/clean_suppliers.csv'
INTO TABLE Suppliers
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Load Purchase Orders
LOAD DATA INFILE
'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/clean_purchase_orders.csv'
INTO TABLE Purchase_Orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Load Invoices

ALTER TABLE Invoices 
MODIFY COLUMN Calculated_Total VARCHAR(50);

ALTER TABLE Invoices 
MODIFY COLUMN Invoice_Discrepancy VARCHAR(50);

LOAD DATA INFILE
'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/clean_invoices.csv'
INTO TABLE Invoices
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Load Inventory

ALTER TABLE Inventory 
MODIFY COLUMN Low_Stock VARCHAR(10);

LOAD DATA INFILE
'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/clean_inventory.csv'
INTO TABLE Inventory
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Load Shipments
LOAD DATA INFILE
'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/clean_shipments.csv'
INTO TABLE Shipments
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Verify Data Loaded
SELECT COUNT(*) FROM Suppliers;

SELECT COUNT(*) FROM Purchase_Orders;

SELECT COUNT(*) FROM Invoices;

SELECT COUNT(*) FROM Inventory;

SELECT COUNT(*) FROM Shipments;

# Test Relationships
SELECT
    p.PO_Number,
    s.Supplier_Name,
    p.Material,
    p.PO_Amount
FROM Purchase_Orders p
JOIN Suppliers s
ON p.Supplier_ID = s.Supplier_ID
LIMIT 10;

