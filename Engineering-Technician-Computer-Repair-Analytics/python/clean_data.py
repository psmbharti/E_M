import pandas as pd
import numpy as np

# ================================
# Step 3: Load Raw Dataset
# ================================

input_file = "data/computer_repairs.csv"
output_file = "data/computer_repairs_clean.csv"

print("Loading dataset...")
df = pd.read_csv(input_file)

print("\n=== HEAD ===")
print(df.head())

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== INFO ===")
print(df.info())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# ================================
# Step 3.5 Remove Duplicate Records
# ================================

print("\nChecking duplicates...")
duplicates = df.duplicated().sum()
print("Duplicate Records:", duplicates)

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)

# ================================
# Step 3.6 Clean Column Names
# ================================

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
)

# ================================
# Step 3.7 Remove Extra Spaces
# ================================

text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# ================================
# Step 3.8 Standardize Brand Names
# ================================

df["Brand"] = df["Brand"].str.title()

# ================================
# Step 3.9 Standardize Failure Categories
# ================================

df["Failure_Category"] = df["Failure_Category"].str.title()

# ================================
# Step 3.10 Convert Date Format
# ================================

df["Repair_Date"] = pd.to_datetime(df["Repair_Date"], errors="coerce")

# ================================
# Step 3.11 Handle Missing Values
# ================================

# Text columns → fill with "Unknown"
for col in text_columns:
    df[col] = df[col].fillna("Unknown")

# Numeric columns → fill with median
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# ================================
# Step 3.12 Validate Repair Hours
# ================================

df.loc[df["Repair_Time_Hours"] <= 0, "Repair_Time_Hours"] = 1

# ================================
# Step 3.13 Validate Repair Cost
# ================================

median_cost = df["Repair_Cost"].median()
df.loc[df["Repair_Cost"] <= 0, "Repair_Cost"] = median_cost

# ================================
# Step 3.14 Validate QC Status
# ================================

valid_qc = ["Pass", "Fail"]

df.loc[
    ~df["QC_Status"].isin(valid_qc),
    "QC_Status"
] = "Fail"

# ================================
# Step 3.15 Validate Customer Satisfaction
# ================================

df["Customer_Satisfaction"] = df["Customer_Satisfaction"].clip(1, 5)

# ================================
# Step 3.16 Data Quality Report
# ================================

quality_report = {
    "Total Records": len(df),
    "Duplicate Records": df.duplicated().sum(),
    "Missing Values": df.isnull().sum().sum(),
    "Columns": len(df.columns)
}

print("\n=== DATA QUALITY REPORT ===")
print(quality_report)

# ================================
# Step 3.17 Save Clean Dataset
# ================================

df.to_csv(output_file, index=False)

print("\nCleaning Completed")
print("Original Records:", df.shape[0])
print("Clean Records:", len(df))
print("File Saved:", output_file)
 