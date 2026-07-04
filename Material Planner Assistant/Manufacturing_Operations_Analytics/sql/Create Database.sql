
# 1 Create Database
CREATE DATABASE ManufacturingDB;
USE ManufacturingDB;

# 2 Create Tables (ERP Structure)

# 1. Manufacturing Orders Table
CREATE TABLE Manufacturing_Orders (
    Order_ID VARCHAR(20),
    Product_ID VARCHAR(20),
    Product_Name VARCHAR(100),
    Customer VARCHAR(100),
    Order_Date DATE,
    Due_Date DATE,
    Manufacturing_Order VARCHAR(20),
    Transfer_Ticket VARCHAR(20),
    Operation VARCHAR(50),
    Work_Center VARCHAR(50),
    Production_Priority VARCHAR(20),
    Quantity INT,
    Completed_Qty INT,
    Pending_Qty INT,
    Production_Status VARCHAR(20),
    Production_Control VARCHAR(50),
    Forecast_Qty INT,
    Actual_Qty INT,
    Forecast_Error INT
);

# Purchase Orders Table
CREATE TABLE Purchase_Orders (
    PO_Number VARCHAR(20),
    Supplier VARCHAR(100),
    PO_Date DATE,
    Item VARCHAR(100),
    Ordered_Qty INT,
    Received_Qty INT,
    PO_Amount DECIMAL(10,2),
    Buyer VARCHAR(50),
    PO_Status VARCHAR(20)
);
# Sales Orders Table
CREATE TABLE Sales_Orders (
    SO_Number VARCHAR(20),
    Customer VARCHAR(100),
    Sales_Date DATE,
    Product VARCHAR(100),
    Order_Qty INT,
    Sales_Amount DECIMAL(10,2),
    Status VARCHAR(20)
);
# Vendor Invoices Table
CREATE TABLE Vendor_Invoices (
    Invoice_ID VARCHAR(20),
    Supplier VARCHAR(100),
    Invoice_Date DATE,
    PO_Number VARCHAR(20),
    Invoice_Amount DECIMAL(10,2),
    PO_Amount DECIMAL(10,2),
    Difference DECIMAL(10,2),
    Validation_Status VARCHAR(20),
    Finance_Status VARCHAR(20)
);
# Load Clean CSV Files into MySQL

# Load Manufacturing Orders
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/manufacturing_orders.csv"
INTO TABLE Manufacturing_Orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Load Purchase Orders
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Purchase_Orders.csv'
INTO TABLE Purchase_Orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Load Sales Orders
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Sales_Orders.csv'
INTO TABLE Sales_Orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Load Vendor Invoices
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/vendor_invoices.csv'
INTO TABLE vendor_invoices
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;















