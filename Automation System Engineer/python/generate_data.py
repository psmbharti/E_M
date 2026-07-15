# Import Libraries
import pandas as pd
import numpy as np
import random
import os
from faker import Faker
from datetime import datetime, timedelta

# Create Faker Object
fake = Faker()

NUM_RECORDS = 500

random.seed(42)
np.random.seed(42)

# Step Master Lists
plants = [
    "Dallas Plant", "Austin Plant", "Houston Plant",
    "Chicago Plant", "Phoenix Plant"
]

production_lines = [
    "Line A", "Line B", "Line C", "Line D",
    "Assembly Line", "Packaging Line"
]

automation_types = ["Fully Automated", "Semi Automated", "Robotic Cell"]

plc_models = [
    "Siemens S7-1500", "Allen Bradley ControlLogix",
    "Mitsubishi FX5U", "Omron NX1P2"
]

scada_systems = ["WinCC", "Ignition", "FactoryTalk", "Wonderware"]

dcs_systems = ["ABB 800xA", "Honeywell Experion", "Emerson DeltaV"]

robot_models = [
    "FANUC M-20iD", "ABB IRB2600",
    "KUKA KR10", "Yaskawa GP25"
]

statuses = ["Running", "Idle", "Maintenance", "Stopped"]

maintenance_status = ["Completed", "Scheduled", "In Progress"]

compliance_status = ["Passed", "Pending", "Failed"]

# Generate Operator IDs
operator_ids = [f"OP{str(i).zfill(3)}" for i in range(1, NUM_RECORDS + 1)]

# Generate Project IDs
project_ids = [f"PRJ{str(i).zfill(3)}" for i in range(1, NUM_RECORDS + 1)]

# Generate PLC IDs
plc_ids = [f"PLC{str(i).zfill(3)}" for i in range(1, NUM_RECORDS + 1)]

# Generate System IDs
system_ids = [f"SYS{str(i).zfill(4)}" for i in range(1, NUM_RECORDS + 1)]

# Generate Automation Systems Dataset
automation_data = []

for i in range(NUM_RECORDS):

    automation_data.append({
        "System_ID": system_ids[i],
        "System_Name": fake.word().title() + " Automation",
        "Plant": random.choice(plants),
        "Production_Line": random.choice(production_lines),
        "Automation_Type": random.choice(automation_types),
        "PLC": plc_ids[i],
        "SCADA": random.choice(scada_systems),
        "DCS": random.choice(dcs_systems),
        "Robot_Model": random.choice(robot_models),
        "Status": random.choice(statuses),
        "Efficiency": round(random.uniform(75, 99), 2),
        "Cycle_Time": round(random.uniform(10, 40), 2),
        "Energy_Consumption": round(random.uniform(500, 2500), 2),
        "Downtime_Minutes": random.randint(0, 300),
        "Alarm_Count": random.randint(0, 15),
        "Operator_ID": operator_ids[i],
        "Maintenance_Status": random.choice(maintenance_status),
        "Project_ID": project_ids[i],
        "Compliance_Status": random.choice(compliance_status),
        "Created_Date": fake.date_between(start_date="-2y", end_date="today")
    })

# Convert to DataFrame
automation_df = pd.DataFrame(automation_data)

# Save CSV
automation_df.to_csv("data/automation_systems.csv", index=False)

print("Automation Systems dataset generated successfully!")
print(f"Total Records: {len(automation_df)}")

# 1. Generate plc_devices.csv

plc_data = []

manufacturers = [
    "Siemens",
    "Allen Bradley",
    "Mitsubishi",
    "Omron"
]

models = [
    "S7-1500",
    "ControlLogix",
    "FX5U",
    "NX1P2"
]

for i in range(NUM_RECORDS):

    plc_data.append({

        "PLC_ID": plc_ids[i],

        "Manufacturer": random.choice(manufacturers),

        "Model": random.choice(models),

        "Firmware": f"V{random.randint(1,5)}.{random.randint(0,9)}",

        "IP_Address": fake.ipv4_private(),

        "CPU_Usage": random.randint(5,95),

        "Memory_Usage": random.randint(10,90),

        "Temperature": round(random.uniform(25,65),1),

        "Voltage": round(random.uniform(22,24),2),

        "Communication_Status": random.choice(
            ["Connected","Disconnected"]
        )

    })

plc_df = pd.DataFrame(plc_data)

plc_df.to_csv("data/plc_devices.csv", index=False)

# 2. Generate scada_logs.csv

tags = [
    "Temperature",
    "Pressure",
    "Speed",
    "Voltage",
    "Current",
    "Flow"
]

logs = []

for i in range(NUM_RECORDS):

    logs.append({

        "Log_ID": f"LOG{str(i+1).zfill(4)}",

        "Timestamp": fake.date_time_between(
            start_date="-90d",
            end_date="now"
        ),

        "System_ID": random.choice(system_ids),

        "Tag_Name": random.choice(tags),

        "Current_Value": round(random.uniform(0,100),2),

        "High_Limit": 95,

        "Low_Limit": 10,

        "Alarm_Status": random.choice(
            ["Normal","Warning","Critical"]
        )

    })

pd.DataFrame(logs).to_csv(
    "data/scada_logs.csv",
    index=False
)

# 3. Generate robots.csv

robot_data = []

robot_manufacturers = [
    "FANUC",
    "ABB",
    "KUKA",
    "Yaskawa"
]

for i in range(NUM_RECORDS):

    robot_data.append({

        "Robot_ID": f"ROB{str(i+1).zfill(4)}",

        "Robot_Model": random.choice(robot_models),

        "Manufacturer": random.choice(robot_manufacturers),

        "Axis_Count": random.choice([4,5,6]),

        "Operating_Hours": random.randint(500,20000),

        "Cycle_Count": random.randint(10000,900000),

        "Error_Code": random.choice(
            ["None","E101","E202","E310"]
        ),

        "Maintenance_Due": fake.date_between(
            start_date="today",
            end_date="+180d"
        ),

        "Status": random.choice(statuses)

    })

pd.DataFrame(robot_data).to_csv(
    "data/robots.csv",
    index=False
)

# 4. Generate sensors.csv

sensor_types = [
    "Temperature",
    "Pressure",
    "Humidity",
    "Flow",
    "Proximity"
]

sensor_data = []

for i in range(NUM_RECORDS):

    sensor_data.append({

        "Sensor_ID": f"SEN{str(i+1).zfill(4)}",

        "System_ID": random.choice(system_ids),

        "Sensor_Type": random.choice(sensor_types),

        "Location": random.choice(plants),

        "Reading": round(random.uniform(0,100),2),

        "Unit": random.choice(
            ["°C","PSI","%","L/min"]
        ),

        "Status": random.choice(
            ["Active","Inactive"]
        ),

        "Calibration_Date": fake.date_between(
            start_date="-1y",
            end_date="today"
        )

    })

pd.DataFrame(sensor_data).to_csv(
    "data/sensors.csv",
    index=False
)
# 5. Generate alarms.csv

alarm_data = []

for i in range(NUM_RECORDS):

    alarm_data.append({

        "Alarm_ID": f"ALM{str(i+1).zfill(4)}",

        "System_ID": random.choice(system_ids),

        "Alarm_Type": random.choice([
            "High Temperature",
            "Low Pressure",
            "Motor Fault",
            "Emergency Stop"
        ]),

        "Severity": random.choice(
            ["Low","Medium","High","Critical"]
        ),

        "Alarm_Time": fake.date_time_this_year(),

        "Cleared_Time": fake.date_time_this_year(),

        "Status": random.choice(
            ["Open","Closed"]
        )

    })

pd.DataFrame(alarm_data).to_csv(
    "data/alarms.csv",
    index=False
)

# 6. Generate maintenance.csv

maintenance = []

for i in range(NUM_RECORDS):

    maintenance.append({

        "Maintenance_ID": f"MT{str(i+1).zfill(4)}",

        "System_ID": random.choice(system_ids),

        "Issue": random.choice([
            "PLC Failure",
            "Sensor Replacement",
            "Robot Calibration",
            "Motor Repair"
        ]),

        "Priority": random.choice(
            ["Low","Medium","High"]
        ),

        "Assigned_Engineer": fake.name(),

        "Status": random.choice(
            ["Completed","Open","In Progress"]
        ),

        "Repair_Time": random.randint(1,24),

        "Cost": round(
            random.uniform(200,5000),2
        ),

        "Completion_Date": fake.date_between(
            start_date="-6M",
            end_date="today"
        )

    })

pd.DataFrame(maintenance).to_csv(
    "data/maintenance.csv",
    index=False
)

# 7. Generate projects.csv

projects = []

for i in range(NUM_RECORDS):

    budget = random.randint(100000,1000000)
    spent = random.randint(50000,budget)

    projects.append({

        "Project_ID": project_ids[i],

        "Project_Name": f"Automation Project {i+1}",

        "Manager": fake.name(),

        "Budget": budget,

        "Spent": spent,

        "Completion": random.randint(10,100),

        "Start_Date": fake.date_between(
            start_date="-2y",
            end_date="-30d"
        ),

        "End_Date": fake.date_between(
            start_date="today",
            end_date="+1y"
        ),

        "Status": random.choice([
            "Planning",
            "Running",
            "Completed"
        ])

    })

pd.DataFrame(projects).to_csv(
    "data/projects.csv",
    index=False
)
# 8. Generate compliance.csv

compliance = []

for i in range(NUM_RECORDS):

    compliance.append({

        "Compliance_ID": f"CMP{str(i+1).zfill(4)}",

        "System_ID": random.choice(system_ids),

        "ISO9001": random.choice(
            ["Pass","Fail"]
        ),

        "ISO27001": random.choice(
            ["Pass","Fail"]
        ),

        "Safety_Check": random.choice(
            ["Pass","Fail"]
        ),

        "Audit_Result": random.choice(
            ["Passed","Failed"]
        ),

        "Inspection_Date": fake.date_between(
            start_date="-1y",
            end_date="today"
        )

    })

pd.DataFrame(compliance).to_csv(
    "data/compliance.csv",
    index=False
)

# 9. Generate operators.csv

operators = []

for i in range(NUM_RECORDS):

    operators.append({

        "Operator_ID": operator_ids[i],

        "Operator_Name": fake.name(),

        "Shift": random.choice([
            "Day",
            "Evening",
            "Night"
        ]),

        "Department": random.choice([
            "Assembly",
            "Packaging",
            "Maintenance",
            "Quality"
        ]),

        "Experience_Years": random.randint(1,25),

        "Certification": random.choice([
            "PLC",
            "SCADA",
            "Robotics",
            "Safety",
            "None"
        ]),

        "Contact": fake.phone_number()

    })

pd.DataFrame(operators).to_csv(
    "data/operators.csv",
    index=False)

