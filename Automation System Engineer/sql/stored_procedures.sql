USE IndustrialAutomationDB;

DELIMITER $$

-- Total Downtime
CREATE PROCEDURE GetTotalDowntime()
BEGIN
    SELECT
    SUM(Downtime_Minutes) AS Total_Downtime
    FROM Automation_Systems;
END $$

-- Plant Performance
CREATE PROCEDURE PlantPerformance()
BEGIN
    SELECT
        Plant,
        AVG(Efficiency) AS Average_Efficiency,
        SUM(Downtime_Minutes) AS Downtime
    FROM Automation_Systems
    GROUP BY Plant;
END $$

-- High CPU PLCs
CREATE PROCEDURE HighCPUControllers()
BEGIN
    SELECT *
    FROM PLC_Devices
    WHERE CPU_Usage > 80;
END $$

-- Maintenance Summary
CREATE PROCEDURE MaintenanceSummary()
BEGIN
    SELECT
        Priority,
        COUNT(*) AS Jobs,
        SUM(Cost) AS Total_Cost
    FROM Maintenance
    GROUP BY Priority;
END $$

-- Compliance Summary
CREATE PROCEDURE ComplianceSummary()
BEGIN
    SELECT
        Audit_Result,
        COUNT(*) AS Total
    FROM Compliance
    GROUP BY Audit_Result;
END $$

DELIMITER ;

-- Execute Procedures
CALL GetTotalDowntime();

CALL PlantPerformance();

CALL HighCPUControllers();

CALL MaintenanceSummary();

CALL ComplianceSummary();