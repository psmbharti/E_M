import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Ensure reproducibility
random.seed(42)
Faker.seed(42)

NUM_RECORDS = 500

# Create Engineering Data Lists
# 1. Device Information
device_types = [
    "Laptop",
    "Desktop",
    "Server",
    "Workstation"
]

brands = [
    "Dell",
    "HP",
    "Lenovo",
    "Apple",
    "Acer",
    "ASUS"
]

models = [
    "Latitude",
    "ThinkPad",
    "EliteBook",
    "MacBook Pro",
    "Aspire",
    "ZenBook"
]
# 2. Failure Information
failure_categories = [
    "Hardware",
    "Software",
    "Network",
    "Power",
    "Display"
]

failure_types = [
    "Motherboard",
    "RAM",
    "SSD",
    "Battery",
    "Screen",
    "Keyboard",
    "Operating System",
    "WiFi Card",
    "Power Supply",
    "Cooling Fan"
]
# 3. Repair Information
repair_actions = [
    "Replace Component",
    "Software Installation",
    "BIOS Update",
    "OS Reinstallation",
    "Cleaning",
    "Firmware Update",
    "Component Repair"
]

parts = [
    "RAM Module",
    "SSD Drive",
    "Battery",
    "Motherboard",
    "Keyboard",
    "Cooling Fan",
    "Power Supply",
    "WiFi Card"
]
# 4. Supplier & Warehouse Information
suppliers = [
    "Samsung",
    "Intel",
    "Kingston",
    "Western Digital",
    "Seagate",
    "Dell Parts"
]

warehouses = [
    "Dallas",
    "Houston",
    "Austin",
    "Phoenix"
]
# 5. Quality Control Information
qc_values = [
    "Pass",
    "Fail"
]

final_status = [
    "Completed",
    "Pending",
    "Cancelled"
]
## Create Empty List
repair_records = []

## Generate 500 Records
for i in range(1, NUM_RECORDS + 1):
    
    repair_id = f"RP{i:06d}"
    device_id = f"DV{random.randint(10000, 99999)}"
    serial_number = fake.bothify(text="SN-????-#####")
    repair_date = datetime.today() - timedelta(days=random.randint(1, 730))

    record = {
        "Repair_ID": repair_id,
        "Device_ID": device_id,
        "Device_Type": random.choice(device_types),
        "Brand": random.choice(brands),
        "Model": random.choice(models),
        "Serial_Number": serial_number,
        "Customer_Name": fake.name(),
        "Engineer": fake.name(),
        "Repair_Date": repair_date.strftime("%Y-%m-%d"),

        "Failure_Category": random.choice(failure_categories),
        "Failure_Type": random.choice(failure_types),
        "Root_Cause": fake.sentence(nb_words=5),

        "Repair_Action": random.choice(repair_actions),
        "Parts_Used": random.choice(parts),

        "Repair_Time_Hours": round(random.uniform(0.5, 10), 2),
        "Repair_Cost": round(random.uniform(50, 800), 2),

        "QC_Status": random.choice(qc_values),
        "QC_Inspector": fake.name(),
        "Rework": random.choice(["Yes", "No"]),
        "Final_Status": random.choice(final_status),

        "Warehouse": random.choice(warehouses),
        "Supplier": random.choice(suppliers),

        "Warranty": random.choice(["Yes", "No"]),
        "Customer_Satisfaction": random.randint(1, 5)
    }

    repair_records.append(record)

# Convert List to DataFrame
df = pd.DataFrame( repair_records)

## Create CSV File
df.to_csv( "data/computer_repairs.csv", index=False )

print(df.head())
print(df.shape)

