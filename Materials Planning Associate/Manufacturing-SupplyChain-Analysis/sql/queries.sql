## Section 1: Basic Data Validation

# 1. Total Records in Each Table
SELECT COUNT(*) AS Total_Suppliers
FROM Suppliers;

SELECT COUNT(*) AS Total_Purchase_Orders
FROM Purchase_Orders;

SELECT COUNT(*) AS Total_Invoices
FROM Invoices;

SELECT COUNT(*) AS Total_Inventory_Items
FROM Inventory;

SELECT COUNT(*) AS Total_Shipments
FROM Shipments;

# 2. Preview Purchase Orders
SELECT *
FROM Purchase_Orders
LIMIT 10;

# 3. Preview Invoices
SELECT *
FROM Invoices
LIMIT 10;

## Section 2: Procurement Analysis

# 4. Total Purchase Spend
SELECT
SUM(PO_Amount) AS Total_Purchase_Value
FROM Purchase_Orders;

# 5. Average Purchase Order Value
SELECT
ROUND(AVG(PO_Amount),2) AS Avg_PO_Value
FROM Purchase_Orders;

# 6. Monthly Procurement Spend
SELECT
YEAR(Order_Date) AS Year,
MONTH(Order_Date) AS Month,
ROUND(SUM(PO_Amount),2) AS Total_Spend
FROM Purchase_Orders
GROUP BY Year, Month
ORDER BY Year, Month;

# 7. Purchase Orders by Status
SELECT Status,
COUNT(*) AS Total_Orders
FROM Purchase_Orders
GROUP BY Status;

## Section 3: Supplier Performance

# 8. Purchase Value by Supplier
SELECT
s.Supplier_Name,
ROUND(SUM(p.PO_Amount),2) AS Purchase_Value
FROM Suppliers s
JOIN Purchase_Orders p
ON s.Supplier_ID = p.Supplier_ID
GROUP BY s.Supplier_Name
ORDER BY Purchase_Value DESC;

# 9. Top 10 Suppliers
SELECT
s.Supplier_Name,
SUM(p.PO_Amount) AS Total_Purchases
FROM Suppliers s
JOIN Purchase_Orders p
ON s.Supplier_ID = p.Supplier_ID
GROUP BY s.Supplier_Name
ORDER BY Total_Purchases DESC
LIMIT 10;

# 10. Average Supplier Rating
SELECT
ROUND(AVG(Supplier_Rating),2)
AS Average_Rating
FROM Suppliers;

# 11. Highest Rated Suppliers
SELECT *
FROM Suppliers
ORDER BY Supplier_Rating DESC;


## Section 4: Invoice Analysis

# 12. Invoice Discrepancies

# Total discrepancy amount
SELECT SUM(Invoice_Discrepancy) AS total_discrepancy
FROM Invoices;

# Group by “range” 
SELECT 
  CASE 
    WHEN Invoice_Discrepancy < 1000 THEN 'Low'
    WHEN Invoice_Discrepancy BETWEEN 1000 AND 10000 THEN 'Medium'
    ELSE 'High'
  END AS discrepancy_level,
  COUNT(*) AS total_invoices
FROM Invoices
GROUP BY discrepancy_level;

# grouping of “similar values”
SELECT 
  ROUND(Invoice_Discrepancy, 0) AS rounded_discrepancy,
  COUNT(*) AS total
FROM Invoices
GROUP BY ROUND(Invoice_Discrepancy, 0);

# 13. Total Invoice Value
SELECT
ROUND(SUM(Final_Amount),2)
AS Total_Invoice_Value
FROM Invoices;

# 14. Payment Status Report
SELECT
Payment_Status,
COUNT(*) AS Total
FROM Invoices
GROUP BY Payment_Status;

# 15. Pending Payments
SELECT *
FROM Invoices
WHERE Calculated_Total='Pending';

## Section 5: Shipment Analysis

# 16. Delayed Shipments
SELECT *
FROM Shipments
WHERE Delay_Days>0;

# 17. Average Delivery Delay
SELECT
ROUND(AVG(Delay_Days),2)
AS Average_Delay
FROM Shipments;

# 18. Top 20 Most Delayed Shipments
SELECT *
FROM Shipments
ORDER BY Delay_Days DESC
LIMIT 20;

# 19. Shipment Status Summary
SELECT
Shipment_Status,
COUNT(*) AS Total
FROM Shipments
GROUP BY Shipment_Status;

## Section 6: Inventory Analysis

# 20. Low Stock Items
SELECT 
    Item_ID,
    Stock,
    Reorder_Level,
    Low_Stock
FROM Inventory
WHERE Stock < Reorder_Level;

 # 22. Total Inventory Value
 SELECT
ROUND(SUM(Inventory_Value),2)
AS Total_Inventory_Value
FROM Inventory;

# 23. Inventory by Warehouse
SELECT
Warehouse,
ROUND(SUM(Inventory_Value),2)
AS Inventory_Value
FROM Inventory
GROUP BY Warehouse;

# 24. Warehouse Stock Levels
SELECT
Warehouse,
SUM(Stock) AS Total_Stock
FROM Inventory
GROUP BY Warehouse;

## Section 7: Supply Chain Analysis

# 25. Supplier Lead Time
SELECT
Supplier_Name,
Lead_Time_Days
FROM Suppliers
ORDER BY Lead_Time_Days;

# 26. Suppliers with Long Lead Time
SELECT *
FROM Suppliers
WHERE Lead_Time_Days>15;

# 27. Purchase Orders with Supplier Information
SELECT
p.PO_Number,
s.Supplier_Name,
p.Material,
p.Quantity,
p.PO_Amount
FROM Purchase_Orders p
JOIN Suppliers s
ON p.Supplier_ID=s.Supplier_ID;

## Section 8: Executive Dashboard KPIs

# 28. Executive KPI Query
SELECT
(SELECT COUNT(*) FROM Suppliers) AS Suppliers,
(SELECT COUNT(*) FROM Purchase_Orders) AS Purchase_Orders,
(SELECT ROUND(SUM(PO_Amount),2)
 FROM Purchase_Orders) AS Purchase_Value,
(SELECT COUNT(*)
 FROM Invoices
 WHERE Invoice_Discrepancy=TRUE) AS Invoice_Errors,
(SELECT COUNT(*)
 FROM Inventory
 WHERE Low_Stock=TRUE) AS Low_Stock_Items,
(SELECT ROUND(SUM(Inventory_Value),2)
 FROM Inventory) AS Inventory_Value;

# 29. Executive Summary
SELECT
ROUND(AVG(Lead_Time_Days),2) AS Avg_Lead_Time,
ROUND(AVG(Supplier_Rating),2) AS Avg_Supplier_Rating,
ROUND(AVG(Delay_Days),2) AS Avg_Delivery_Delay
FROM Suppliers, Shipments;

# 30. Complete Supply Chain Report
SELECT
p.PO_Number,
s.Supplier_Name,
p.Material,
p.Quantity,
p.PO_Amount,
i.Final_Amount,
i.Payment_Status,
sh.Delay_Days,
sh.Shipment_Status

FROM Purchase_Orders p

JOIN Suppliers s
ON p.Supplier_ID=s.Supplier_ID

JOIN Invoices i
ON p.PO_Number=i.PO_Number

JOIN Shipments sh
ON p.PO_Number=sh.PO_Number;
