## Data Validation Queries
# Check Row Counts
SELECT 'Manufacturing' AS TableName, COUNT(*) FROM Manufacturing_Orders
UNION
SELECT 'Purchase', COUNT(*) FROM Purchase_Orders
UNION
SELECT 'Sales', COUNT(*) FROM Sales_Orders
UNION
SELECT 'Invoices', COUNT(*) FROM Vendor_Invoices;

## KPI QUERIES 

# KPI 1: Delay %
SELECT 
    ROUND(
        (SUM(CASE WHEN Production_Status = 'Delayed' THEN 1 ELSE 0 END) 
        / COUNT(*)) * 100, 2
    ) AS Delay_Percentage
FROM Manufacturing_Orders;

# KPI 2: Production Efficiency
SELECT 
    ROUND(
        SUM(Completed_Qty) / SUM(Quantity) * 100, 2
    ) AS Production_Efficiency
FROM Manufacturing_Orders;

# KPI 3: Supplier Performance (Based on PO completion)
SELECT 
    Supplier,
    SUM(Ordered_Qty) AS Total_Ordered,
    SUM(Received_Qty) AS Total_Received,
    ROUND(SUM(Received_Qty)/SUM(Ordered_Qty)*100,2) AS Fulfillment_Rate
FROM Purchase_Orders
GROUP BY Supplier
ORDER BY Fulfillment_Rate DESC;

# KPI 4: Invoice Mismatch Rate
SELECT 
    ROUND(
        (SUM(CASE WHEN Validation_Status = 'Mismatch' THEN 1 ELSE 0 END)
        / COUNT(*)) * 100, 2
    ) AS Invoice_Mismatch_Rate
FROM Vendor_Invoices;

# KPI 5: Top Customers by Sales
SELECT 
    Customer,
    SUM(Sales_Amount) AS Total_Sales
FROM Sales_Orders
GROUP BY Customer
ORDER BY Total_Sales DESC;

# KPI 6: Work Center Load (Bottleneck Analysis)

SELECT 
    Work_Center,
    COUNT(*) AS Total_Orders
FROM Manufacturing_Orders
GROUP BY Work_Center
ORDER BY Total_Orders DESC;

# KPI 7: PO vs Invoice Difference
SELECT 
    Supplier,
    SUM(PO_Amount) AS PO_Total,
    SUM(Invoice_Amount) AS Invoice_Total,
    SUM(Difference) AS Total_Variance
FROM Vendor_Invoices
GROUP BY Supplier;

## Advanced JOIN Query (REAL ERP VIEW)

# Full Manufacturing + PO + Invoice View
SELECT 
    m.Order_ID,
    m.Product_Name,
    m.Customer,
    m.Production_Status,
    p.PO_Number,
    p.Supplier,
    v.Invoice_ID,
    v.Validation_Status,
    v.Finance_Status
FROM Manufacturing_Orders m
JOIN Purchase_Orders p
    ON m.Product_Name = p.Item
JOIN Vendor_Invoices v
    ON p.PO_Number = v.PO_Number;














