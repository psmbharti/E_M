import pandas as pd
import numpy as np
import os

# ---------------------------------------------------
# File Locations
# ---------------------------------------------------

DATA_PATH = "data/cleaned/"
OUTPUT_PATH = "data/analysis/"

os.makedirs(OUTPUT_PATH, exist_ok=True)

# ---------------------------------------------------
# Load Data Function
# ---------------------------------------------------

def load_file(filename):
    return pd.read_csv(DATA_PATH + filename)

# ---------------------------------------------------
# Load Datasets
# ---------------------------------------------------

systems = load_file("automation_systems_clean.csv")
plc = load_file("plc_devices_clean.csv")
robots = load_file("robots_clean.csv")
alarms = load_file("alarms_clean.csv")
maintenance = load_file("maintenance_clean.csv")
projects = load_file("projects_clean.csv")
compliance = load_file("compliance_clean.csv")

# ---------------------------------------------------
# KPI 1: System Performance
# ---------------------------------------------------

system_kpi = {
    "Total Systems": len(systems),
    "Average Efficiency": round(systems["Efficiency"].mean(), 2),
    "Average Cycle Time": round(systems["Cycle_Time"].mean(), 2),
    "Total Downtime Minutes": systems["Downtime_Minutes"].sum(),
    "Total Alarms": systems["Alarm_Count"].sum()
}

system_kpi_df = pd.DataFrame(system_kpi.items(), columns=["KPI", "Value"])
system_kpi_df.to_csv(OUTPUT_PATH + "system_kpi.csv", index=False)

# ---------------------------------------------------
# KPI 2: PLC Performance Analysis
# ---------------------------------------------------

plc_analysis = plc.groupby("Manufacturer").agg(
    Average_CPU=("CPU_Usage", "mean"),
    Average_Memory=("Memory_Usage", "mean"),
    Average_Temperature=("Temperature", "mean")
).reset_index()

plc_analysis.to_csv(OUTPUT_PATH + "plc_analysis.csv", index=False)

# ---------------------------------------------------
# KPI 3: Robot Utilization
# ---------------------------------------------------

robot_analysis = robots.groupby("Manufacturer").agg(
    Total_Robots=("Robot_ID", "count"),
    Operating_Hours=("Operating_Hours", "sum"),
    Total_Cycles=("Cycle_Count", "sum")
).reset_index()

robot_analysis.to_csv(OUTPUT_PATH + "robot_analysis.csv", index=False)

# ---------------------------------------------------
# KPI 4: Alarm Analysis
# ---------------------------------------------------

alarm_analysis = alarms.groupby("Severity").size().reset_index(name="Alarm_Count")
alarm_analysis.to_csv(OUTPUT_PATH + "alarm_analysis.csv", index=False)

# ---------------------------------------------------
# KPI 5: Maintenance Cost
# ---------------------------------------------------

maintenance_analysis = maintenance.groupby("Priority").agg(
    Total_Cost=("Cost", "sum"),
    Average_Repair_Time=("Repair_Time", "mean")
).reset_index()

maintenance_analysis.to_csv(OUTPUT_PATH + "maintenance_analysis.csv", index=False)

# ---------------------------------------------------
# KPI 6: Compliance Analysis
# ---------------------------------------------------

compliance_analysis = compliance.groupby("Audit_Result").size().reset_index(name="Count")
compliance_analysis.to_csv(OUTPUT_PATH + "compliance_analysis.csv", index=False)

# ---------------------------------------------------
# KPI 7: Project Performance
# ---------------------------------------------------

project_analysis = projects.groupby("Status").agg(
    Projects=("Project_ID", "count"),
    Average_Completion=("Completion", "mean")
).reset_index()

project_analysis.to_csv(OUTPUT_PATH + "project_analysis.csv", index=False)

# ---------------------------------------------------
# Final Message
# ---------------------------------------------------

print("Automation Analysis Completed")
