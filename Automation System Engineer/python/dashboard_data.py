import pandas as pd
import os

# ---------------------------------------------------
# File Paths
# ---------------------------------------------------

INPUT = "data/cleaned/"
OUTPUT = "data/dashboard/"

os.makedirs(OUTPUT, exist_ok=True)

# ---------------------------------------------------
# Executive Dashboard Dataset
# ---------------------------------------------------

systems = pd.read_csv(INPUT + "automation_systems_clean.csv")

dashboard = systems[
    [
        "System_ID",
        "Plant",
        "Production_Line",
        "Status",
        "Efficiency",
        "Cycle_Time",
        "Energy_Consumption",
        "Downtime_Minutes"
    ]
]

dashboard.to_csv(OUTPUT + "executive_dashboard.csv", index=False)

# ---------------------------------------------------
# PLC Dashboard
# ---------------------------------------------------

plc = pd.read_csv(INPUT + "plc_devices_clean.csv")
plc.to_csv(OUTPUT + "plc_dashboard.csv", index=False)

# ---------------------------------------------------
# Robotics Dashboard
# ---------------------------------------------------

robots = pd.read_csv(INPUT + "robots_clean.csv")
robots.to_csv(OUTPUT + "robot_dashboard.csv", index=False)

# ---------------------------------------------------
# Maintenance Dashboard
# ---------------------------------------------------

maintenance = pd.read_csv(INPUT + "maintenance_clean.csv")
maintenance.to_csv(OUTPUT + "maintenance_dashboard.csv", index=False)

# ---------------------------------------------------
# Compliance Dashboard
# ---------------------------------------------------

compliance = pd.read_csv(INPUT + "compliance_clean.csv")
compliance.to_csv(OUTPUT + "compliance_dashboard.csv", index=False)

# ---------------------------------------------------
# Final Message
# ---------------------------------------------------

print("Dashboard datasets generated successfully")
