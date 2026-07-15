import pandas as pd
import os
from datetime import datetime

# ---------------------------------------------------
# Step 4.2 File Paths
# ---------------------------------------------------

DATA_PATH = "data/cleaned/"
REPORT_PATH = "documentation/"

os.makedirs(REPORT_PATH, exist_ok=True)

# ---------------------------------------------------
# Step 4.3 Load Data
# ---------------------------------------------------

def load_data(filename):
    return pd.read_csv(DATA_PATH + filename)

# ---------------------------------------------------
# Step 4.4 Create Test Result Function
# ---------------------------------------------------

test_results = []

def add_result(test_id, test_name, expected, actual, status, comments):
    test_results.append({
        "Test_ID": test_id,
        "Test_Name": test_name,
        "Expected_Result": expected,
        "Actual_Result": actual,
        "Status": status,
        "Comments": comments,
        "Test_Date": datetime.now()
    })

# ---------------------------------------------------
# FAT TESTING
# ---------------------------------------------------

# FAT001 – Automation System ID Validation
systems = load_data("automation_systems_clean.csv")

duplicate_systems = systems["System_ID"].duplicated().sum()

if duplicate_systems == 0:
    add_result("FAT001", "System ID Validation",
               "Unique System IDs", "All IDs Unique",
               "PASS", "No duplicate system IDs found")
else:
    add_result("FAT001", "System ID Validation",
               "Unique System IDs", f"{duplicate_systems} duplicates",
               "FAIL", "Duplicate IDs detected")

# FAT002 – PLC CPU Validation
plc = load_data("plc_devices_clean.csv")

high_cpu = plc[plc["CPU_Usage"] > 90]

if len(high_cpu) == 0:
    add_result("FAT002", "PLC CPU Test",
               "<90%", "All PLC CPUs Normal",
               "PASS", "PLC performance acceptable")
else:
    add_result("FAT002", "PLC CPU Test",
               "<90%", f"{len(high_cpu)} high CPU PLCs",
               "FAIL", "CPU overload detected")

# FAT003 – PLC Communication Test
communication_errors = plc[plc["Communication_Status"] != "Connected"]

if len(communication_errors) == 0:
    add_result("FAT003", "PLC Communication",
               "Connected", "All Connected",
               "PASS", "Communication test successful")
else:
    add_result("FAT003", "PLC Communication",
               "Connected", f"{len(communication_errors)} failures",
               "FAIL", "Network issues detected")

# FAT004 – Sensor Calibration Test
sensors = load_data("sensors_clean.csv")

missing_calibration = sensors[sensors["Calibration_Date"].isna()]

if len(missing_calibration) == 0:
    add_result("FAT004", "Sensor Calibration",
               "Valid Calibration Date", "All Sensors Calibrated",
               "PASS", "Calibration verified")
else:
    add_result("FAT004", "Sensor Calibration",
               "Valid Calibration Date", f"{len(missing_calibration)} missing",
               "FAIL", "Calibration problem")

# FAT005 – Robot Configuration Test
robots = load_data("robots_clean.csv")

invalid_robot = robots[~robots["Axis_Count"].isin([4, 5, 6])]

if len(invalid_robot) == 0:
    add_result("FAT005", "Robot Configuration",
               "4-6 Axis Robot", "Valid",
               "PASS", "Robot configuration approved")
else:
    add_result("FAT005", "Robot Configuration",
               "4-6 Axis Robot", "Invalid Configuration",
               "FAIL", "Robot setup error")

# ---------------------------------------------------
# SAT TESTING
# ---------------------------------------------------

# SAT001 – System Availability
stopped_systems = systems[systems["Status"] == "Stopped"]

if len(stopped_systems) == 0:
    add_result("SAT001", "System Availability",
               "No stopped systems", "All Systems Running",
               "PASS", "Production ready")
else:
    add_result("SAT001", "System Availability",
               "No stopped systems", f"{len(stopped_systems)} stopped",
               "FAIL", "Production issue")

# SAT002 – Alarm Verification
alarms = load_data("alarms_clean.csv")

open_alarm = alarms[alarms["Status"] == "Open"]

if len(open_alarm) < 50:
    add_result("SAT002", "Alarm Verification",
               "<50 Open Alarms", f"{len(open_alarm)} Open",
               "PASS", "Alarm level acceptable")
else:
    add_result("SAT002", "Alarm Verification",
               "<50 Open Alarms", f"{len(open_alarm)} Open",
               "FAIL", "Too many active alarms")

# SAT003 – Maintenance Readiness
maintenance = load_data("maintenance_clean.csv")

open_tasks = maintenance[maintenance["Status"] == "Open"]

if len(open_tasks) < 100:
    add_result("SAT003", "Maintenance Readiness",
               "<100 Open Tasks", f"{len(open_tasks)} Tasks",
               "PASS", "Maintenance acceptable")
else:
    add_result("SAT003", "Maintenance Readiness",
               "<100 Open Tasks", f"{len(open_tasks)} Tasks",
               "FAIL", "Maintenance backlog")

# SAT004 – Compliance Verification
compliance = load_data("compliance_clean.csv")

failed = compliance[compliance["Audit_Result"] == "Failed"]

if len(failed) == 0:
    add_result("SAT004", "Compliance Test",
               "No Failed Audits", "Compliant",
               "PASS", "Safety requirements met")
else:
    add_result("SAT004", "Compliance Test",
               "No Failed Audits", f"{len(failed)} Failed",
               "FAIL", "Compliance issues found")

# ---------------------------------------------------
# Step 4.5 Generate FAT/SAT Report
# ---------------------------------------------------

report = pd.DataFrame(test_results)

report.to_csv(REPORT_PATH + "FAT_SAT_Test_Report.csv", index=False)

print("FAT/SAT Validation Completed")
