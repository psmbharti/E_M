## (Creates reusable engineering views)

USE Engineering_Repair_DB;

CREATE VIEW Quality_Performance AS
SELECT
    QC_Status,
    COUNT(*) AS Total_Repairs,
    AVG(Repair_Cost) AS Avg_Cost,
    AVG(Repair_Time_Hours) AS Avg_Time
FROM Computer_Repairs
GROUP BY QC_Status;

CREATE VIEW Technician_Performance AS
SELECT
    Engineer,
    COUNT(*) AS Repairs_Completed,
    AVG(Repair_Time_Hours) AS Avg_Repair_Time,
    AVG(Customer_Satisfaction) AS Avg_Rating
FROM Computer_Repairs
GROUP BY Engineer;

CREATE VIEW Failure_Analysis AS
SELECT
    Failure_Type,
    COUNT(*) AS Failure_Count
FROM Computer_Repairs
GROUP BY Failure_Type
ORDER BY Failure_Count DESC;

CREATE VIEW Warehouse_Efficiency AS
SELECT
    Warehouse,
    COUNT(*) AS Repairs,
    AVG(Repair_Time_Hours) AS Avg_Time,
    AVG(Repair_Cost) AS Avg_Cost
FROM Computer_Repairs
GROUP BY Warehouse;

CREATE VIEW Supplier_Reliability AS
SELECT
    Supplier,
    COUNT(*) AS Repairs,
    AVG(Customer_Satisfaction) AS Avg_Satisfaction,
    AVG(Repair_Cost) AS Avg_Cost
FROM Computer_Repairs
GROUP BY Supplier;
