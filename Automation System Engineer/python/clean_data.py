import pandas as pd
import numpy as np
import os

# ---------------------------------------------------
# Step 3.2 Create Clean Data Folder
# ---------------------------------------------------

RAW_PATH = "data/"
CLEAN_PATH = "data/cleaned/"

os.makedirs(CLEAN_PATH, exist_ok=True)

# ---------------------------------------------------
# Step 3.3 Load CSV Function
# ---------------------------------------------------

def load_csv(filename):
    path = RAW_PATH + filename
    df = pd.read_csv(path)
    print(filename, "Loaded:", df.shape)
    return df

# ---------------------------------------------------
# Step 3.4 Remove Duplicate Records
# ---------------------------------------------------

def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print("Duplicates Removed:", before - after)
    return df

# ---------------------------------------------------
# Step 3.5 Standardize Text Columns
# ---------------------------------------------------

def clean_text(df):
    text_columns = df.select_dtypes(include="object").columns

    for col in text_columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )
    return df

# ---------------------------------------------------
# Step 3.6 Handle Missing Values
# ---------------------------------------------------

def handle_missing(df):
    for col in df.columns:
        if df[col].dtype == "object":
            df[col].fillna("Unknown", inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)
    return df

# ---------------------------------------------------
# Step 3.7 Validate Automation System Data
# ---------------------------------------------------

def validate_systems(df):

    df.loc[(df["Efficiency"] > 100), "Efficiency"] = 100
    df.loc[(df["Efficiency"] < 0), "Efficiency"] = 0

    df.loc[(df["Cycle_Time"] <= 0), "Cycle_Time"] = df["Cycle_Time"].median()

    df.loc[(df["Energy_Consumption"] < 0), "Energy_Consumption"] = 0

    return df

# ---------------------------------------------------
# Step 3.8 Validate PLC Data
# ---------------------------------------------------

def validate_plc(df):

    limits = ["CPU_Usage", "Memory_Usage"]

    for col in limits:
        df.loc[df[col] > 100, col] = 100
        df.loc[df[col] < 0, col] = 0

    return df

# ---------------------------------------------------
# Step 3.9 Date Standardization
# ---------------------------------------------------

def clean_dates(df):
    for col in df.columns:
        # Only convert REAL date columns
        if col.endswith("_Date") or col.endswith("_Timestamp"):
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


# ---------------------------------------------------
# Step 3.10 Generate Data Quality Report
# ---------------------------------------------------

def create_report(df, name):
    report = {
        "Dataset": name,
        "Rows": len(df),
        "Columns": len(df.columns),
        "Duplicate_Count": df.duplicated().sum(),
        "Missing_Values": df.isnull().sum().sum()
    }
    return report

# ---------------------------------------------------
# Step 3.11 Process Automation Systems
# ---------------------------------------------------

reports = []

systems = load_csv("automation_systems.csv")
systems = remove_duplicates(systems)
systems = clean_text(systems)
systems = handle_missing(systems)
systems = validate_systems(systems)
systems = clean_dates(systems)

systems.to_csv(CLEAN_PATH + "automation_systems_clean.csv", index=False)

reports.append(create_report(systems, "automation_systems"))

# ---------------------------------------------------
# Step 3.12 Process PLC Dataset
# ---------------------------------------------------

plc = load_csv("plc_devices.csv")
plc = remove_duplicates(plc)
plc = clean_text(plc)
plc = handle_missing(plc)
plc = validate_plc(plc)
plc = clean_dates(plc)

plc.to_csv(CLEAN_PATH + "plc_devices_clean.csv", index=False)

reports.append(create_report(plc, "plc_devices"))

# ---------------------------------------------------
# Step 3.13 Generic Cleaning For Remaining Files
# ---------------------------------------------------

files = [
    "scada_logs.csv",
    "robots.csv",
    "sensors.csv",
    "alarms.csv",
    "maintenance.csv",
    "projects.csv",
    "compliance.csv",
    "operators.csv"
]

for file in files:
    df = load_csv(file)
    df = remove_duplicates(df)
    df = clean_text(df)
    df = handle_missing(df)
    df = clean_dates(df)

    output = file.replace(".csv", "_clean.csv")

    df.to_csv(CLEAN_PATH + output, index=False)

    reports.append(create_report(df, file))

# ---------------------------------------------------
# Step 3.14 Save Quality Report
# ---------------------------------------------------

report_df = pd.DataFrame(reports)
report_df.to_csv(CLEAN_PATH + "data_quality_report.csv", index=False)

print("Cleaning Completed Successfully")
