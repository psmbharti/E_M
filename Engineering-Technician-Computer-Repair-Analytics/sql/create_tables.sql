create database Engineering_Repair_DB;
USE Engineering_Repair_DB;

CREATE TABLE Computer_Repairs (
    Repair_ID VARCHAR(20) PRIMARY KEY,
    Device_ID VARCHAR(20),
    Device_Type VARCHAR(50),
    Brand VARCHAR(50),
    Model VARCHAR(50),
    Serial_Number VARCHAR(50) UNIQUE,
    Customer_Name VARCHAR(100),
    Engineer VARCHAR(100),
    Repair_Date DATE,
    Failure_Category VARCHAR(50),
    Failure_Type VARCHAR(100),
    Root_Cause TEXT,
    Repair_Action VARCHAR(100),
    Parts_Used VARCHAR(100),
    Repair_Time_Hours DECIMAL(5,2),
    Repair_Cost DECIMAL(10,2),
    QC_Status VARCHAR(20),
    QC_Inspector VARCHAR(100),
    Rework VARCHAR(10),
    Final_Status VARCHAR(20),
    Warehouse VARCHAR(50),
    Supplier VARCHAR(100),
    Warranty VARCHAR(10),
    Customer_Satisfaction INT
);

CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY,
    Employee_Name VARCHAR(100),
    Department VARCHAR(50),
    Role VARCHAR(50),
    Experience_Years INT
);

CREATE TABLE Suppliers (
    Supplier_ID INT PRIMARY KEY,
    Supplier_Name VARCHAR(100),
    Rating DECIMAL(3,2),
    Lead_Time_Days INT
);

CREATE TABLE Warehouses (
    Warehouse_ID INT PRIMARY KEY,
    Warehouse_Name VARCHAR(50),
    Location VARCHAR(100),
    Capacity INT
);

CREATE TABLE Parts (
    Part_ID INT PRIMARY KEY,
    Part_Name VARCHAR(100),
    Supplier_ID INT,
    Cost DECIMAL(10,2),
    FOREIGN KEY (Supplier_ID) REFERENCES Suppliers(Supplier_ID)
);
SHOW VARIABLES LIKE 'local_infile'; 