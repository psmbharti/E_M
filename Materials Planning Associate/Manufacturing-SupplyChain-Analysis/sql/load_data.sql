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

