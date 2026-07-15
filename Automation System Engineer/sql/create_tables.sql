-- ============================================
-- Create Database
-- ============================================

CREATE DATABASE IF NOT EXISTS IndustrialAutomationDB;

USE IndustrialAutomationDB;

-- ============================================
-- Automation Systems
-- ============================================

CREATE TABLE Automation_Systems (

    System_ID VARCHAR(10) PRIMARY KEY,

    System_Name VARCHAR(100),

    Plant VARCHAR(100),

    Production_Line VARCHAR(100),

    Automation_Type VARCHAR(50),

    PLC VARCHAR(20),

    SCADA VARCHAR(50),

    DCS VARCHAR(50),

    Robot_Model VARCHAR(50),

    Status VARCHAR(30),

    Efficiency DECIMAL(5,2),

    Cycle_Time DECIMAL(8,2),

    Energy_Consumption DECIMAL(10,2),

    Downtime_Minutes INT,

    Alarm_Count INT,

    Operator_ID VARCHAR(10),

    Maintenance_Status VARCHAR(30),

    Project_ID VARCHAR(10),

    Compliance_Status VARCHAR(20),

    Created_Date DATE
);

-- ============================================

CREATE TABLE PLC_Devices (

    PLC_ID VARCHAR(20) PRIMARY KEY,

    Manufacturer VARCHAR(50),

    Model VARCHAR(50),

    Firmware VARCHAR(20),

    IP_Address VARCHAR(30),

    CPU_Usage DECIMAL(5,2),

    Memory_Usage DECIMAL(5,2),

    Temperature DECIMAL(5,2),

    Voltage DECIMAL(5,2),

    Communication_Status VARCHAR(30)
);

-- ============================================

CREATE TABLE SCADA_Logs (

    Log_ID VARCHAR(20) PRIMARY KEY,

    Timestamp DATETIME,

    System_ID VARCHAR(10),

    Tag_Name VARCHAR(50),

    Current_Value DECIMAL(10,2),

    High_Limit DECIMAL(10,2),

    Low_Limit DECIMAL(10,2),

    Alarm_Status VARCHAR(30),

    FOREIGN KEY (System_ID)
    REFERENCES Automation_Systems(System_ID)
);

-- ============================================

CREATE TABLE Robots (

    Robot_ID VARCHAR(20) PRIMARY KEY,

    Robot_Model VARCHAR(50),

    Manufacturer VARCHAR(50),

    Axis_Count INT,

    Operating_Hours INT,

    Cycle_Count INT,

    Error_Code VARCHAR(20),

    Maintenance_Due DATE,

    Status VARCHAR(30)
);

-- ============================================

CREATE TABLE Sensors (

    Sensor_ID VARCHAR(20) PRIMARY KEY,

    System_ID VARCHAR(10),

    Sensor_Type VARCHAR(50),

    Location VARCHAR(100),

    Reading DECIMAL(10,2),

    Unit VARCHAR(20),

    Status VARCHAR(30),

    Calibration_Date DATE,

    FOREIGN KEY (System_ID)
    REFERENCES Automation_Systems(System_ID)
);

-- ============================================

CREATE TABLE Alarms (

    Alarm_ID VARCHAR(20) PRIMARY KEY,

    System_ID VARCHAR(10),

    Alarm_Type VARCHAR(100),

    Severity VARCHAR(20),

    Alarm_Time DATETIME,

    Cleared_Time DATETIME,

    Status VARCHAR(20),

    FOREIGN KEY (System_ID)
    REFERENCES Automation_Systems(System_ID)
);

-- ============================================

CREATE TABLE Maintenance (

    Maintenance_ID VARCHAR(20) PRIMARY KEY,

    System_ID VARCHAR(10),

    Issue VARCHAR(100),

    Priority VARCHAR(20),

    Assigned_Engineer VARCHAR(100),

    Status VARCHAR(30),

    Repair_Time INT,

    Cost DECIMAL(10,2),

    Completion_Date DATE,

    FOREIGN KEY (System_ID)
    REFERENCES Automation_Systems(System_ID)
);

-- ============================================

CREATE TABLE Projects (

    Project_ID VARCHAR(10) PRIMARY KEY,

    Project_Name VARCHAR(100),

    Manager VARCHAR(100),

    Budget DECIMAL(12,2),

    Spent DECIMAL(12,2),

    Completion INT,

    Start_Date DATE,

    End_Date DATE,

    Status VARCHAR(30)
);

-- ============================================

CREATE TABLE Compliance (

    Compliance_ID VARCHAR(20) PRIMARY KEY,

    System_ID VARCHAR(10),

    ISO9001 VARCHAR(10),

    ISO27001 VARCHAR(10),

    Safety_Check VARCHAR(10),

    Audit_Result VARCHAR(20),

    Inspection_Date DATE,

    FOREIGN KEY (System_ID)
    REFERENCES Automation_Systems(System_ID)
);

-- ============================================

CREATE TABLE Operators (

    Operator_ID VARCHAR(10) PRIMARY KEY,

    Operator_Name VARCHAR(100),

    Shift VARCHAR(20),

    Department VARCHAR(50),

    Experience_Years INT,

    Certification VARCHAR(50),

    Contact VARCHAR(50)
);