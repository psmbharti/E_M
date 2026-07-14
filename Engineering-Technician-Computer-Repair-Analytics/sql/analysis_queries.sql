## (All engineering analysis queries)

USE Engineering_Repair_DB;

-- Total Repairs
SELECT COUNT(*) AS Total_Repairs
FROM Computer_Repairs;

-- QC Pass vs Fail
SELECT QC_Status, COUNT(*) AS Count
FROM Computer_Repairs
GROUP BY QC_Status;

-- Top Failure Types
SELECT Failure_Type, COUNT(*) AS Failures
FROM Computer_Repairs
GROUP BY Failure_Type
ORDER BY Failures DESC;

-- Average Repair Cost by Brand
SELECT Brand, ROUND(AVG(Repair_Cost), 2) AS Avg_Cost
FROM Computer_Repairs
GROUP BY Brand;

-- Warehouse Efficiency
SELECT Warehouse, COUNT(*) AS Repairs,
       ROUND(AVG(Repair_Time_Hours), 2) AS Avg_Time
FROM Computer_Repairs
GROUP BY Warehouse;

-- Rework Analysis
SELECT Rework, COUNT(*) AS Total
FROM Computer_Repairs
GROUP BY Rework;

-- Supplier Quality
SELECT Supplier, COUNT(*) AS Repairs,
       AVG(Customer_Satisfaction) AS Avg_Rating
FROM Computer_Repairs
GROUP BY Supplier;

-- MTTR (Mean Time to Repair)
SELECT AVG(Repair_Time_Hours) AS MTTR
FROM Computer_Repairs;

-- Median Repair Time
SELECT
    AVG(Repair_Time_Hours) AS Median_Repair_Time
FROM (
    SELECT
        Repair_Time_Hours,
        ROW_NUMBER() OVER (ORDER BY Repair_Time_Hours) AS row_num,
        COUNT(*) OVER () AS total_rows
    FROM Computer_Repairs
) AS t
WHERE 
    row_num IN (FLOOR((total_rows + 1) / 2), CEIL((total_rows + 1) / 2));

-- Cost per Category
SELECT Failure_Category, AVG(Repair_Cost) AS Avg_Cost
FROM Computer_Repairs
GROUP BY Failure_Category;
