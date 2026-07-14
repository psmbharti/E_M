import pandas as pd
import os

# ============================================
# Step 4.3 Load Clean Dataset
# ============================================

input_file = "data/computer_repairs_clean.csv"
df = pd.read_csv(input_file)

print("=== Loaded Clean Dataset ===")
print(df.head())

# ============================================
# Step 4.4 Create Validation Results List
# ============================================

validation_results = []

# ============================================
# Step 4.5 Validate Repair ID (Unique)
# ============================================

repair_id_check = {
    "Validation": "Repair ID Unique",
    "Status": "PASS" if df["Repair_ID"].is_unique else "FAIL",
    "Failed_Count": df["Repair_ID"].duplicated().sum()
}

validation_results.append(repair_id_check)

# ============================================
# Step 4.6 Validate Device ID (Missing Check)
# ============================================

device_check = {
    "Validation": "Device ID Missing Check",
    "Status": "PASS" if df["Device_ID"].isnull().sum() == 0 else "FAIL",
    "Failed_Count": df["Device_ID"].isnull().sum()
}

validation_results.append(device_check)

# ============================================
# Step 4.7 Validate Serial Numbers (Unique)
# ============================================

serial_duplicates = df["Serial_Number"].duplicated().sum()

serial_check = {
    "Validation": "Serial Number Unique",
    "Status": "PASS" if serial_duplicates == 0 else "FAIL",
    "Failed_Count": serial_duplicates
}

validation_results.append(serial_check)

# ============================================
# Step 4.8 Validate Repair Dates (No Future Dates)
# ============================================

future_dates = df[pd.to_datetime(df["Repair_Date"]) > pd.Timestamp.today()]

date_check = {
    "Validation": "Future Repair Date Check",
    "Status": "PASS" if len(future_dates) == 0 else "FAIL",
    "Failed_Count": len(future_dates)
}

validation_results.append(date_check)

# ============================================
# Step 4.9 Validate Repair Time (0.1 to 24 hours)
# ============================================

invalid_time = df[
    (df["Repair_Time_Hours"] <= 0) |
    (df["Repair_Time_Hours"] > 24)
]

time_check = {
    "Validation": "Repair Time Range",
    "Status": "PASS" if len(invalid_time) == 0 else "FAIL",
    "Failed_Count": len(invalid_time)
}

validation_results.append(time_check)

# ============================================
# Step 4.10 Validate Repair Cost (> 0)
# ============================================

invalid_cost = df[df["Repair_Cost"] <= 0]

cost_check = {
    "Validation": "Repair Cost Validation",
    "Status": "PASS" if len(invalid_cost) == 0 else "FAIL",
    "Failed_Count": len(invalid_cost)
}

validation_results.append(cost_check)

# ============================================
# Step 4.11 Validate QC Status (Pass/Fail)
# ============================================

invalid_qc = df[~df["QC_Status"].isin(["Pass", "Fail"])]

qc_check = {
    "Validation": "QC Status Validation",
    "Status": "PASS" if len(invalid_qc) == 0 else "FAIL",
    "Failed_Count": len(invalid_qc)
}

validation_results.append(qc_check)

# ============================================
# Step 4.12 Validate Warehouse Values
# ============================================

valid_warehouses = ["Dallas", "Houston", "Austin", "Phoenix"]

invalid_warehouse = df[~df["Warehouse"].isin(valid_warehouses)]

warehouse_check = {
    "Validation": "Warehouse Validation",
    "Status": "PASS" if len(invalid_warehouse) == 0 else "FAIL",
    "Failed_Count": len(invalid_warehouse)
}

validation_results.append(warehouse_check)

# ============================================
# Step 4.13 Validate Customer Satisfaction (1–5)
# ============================================

invalid_rating = df[~df["Customer_Satisfaction"].between(1, 5)]

rating_check = {
    "Validation": "Customer Rating Validation",
    "Status": "PASS" if len(invalid_rating) == 0 else "FAIL",
    "Failed_Count": len(invalid_rating)
}

validation_results.append(rating_check)

# ============================================
# Step 4.14 Create Validation Report
# ============================================

validation_df = pd.DataFrame(validation_results)

print("\n=== VALIDATION REPORT ===")
print(validation_df)

# ============================================
# Step 4.15 Save Validation Report
# ============================================

os.makedirs("../reports", exist_ok=True)

validation_df.to_csv("reports/validation_report.csv", index=False)

# ============================================
# Step 4.16 Create Quality Metrics Report
# ============================================

quality_metrics = {
    "Total Repairs": len(df),
    "QC Pass Count": len(df[df["QC_Status"] == "Pass"]),
    "QC Fail Count": len(df[df["QC_Status"] == "Fail"]),
    "Average Repair Time": round(df["Repair_Time_Hours"].mean(), 2),
    "Average Repair Cost": round(df["Repair_Cost"].mean(), 2)
}

quality_df = pd.DataFrame([quality_metrics])

quality_df.to_csv("reports/quality_test_report.csv", index=False)

# ============================================
# Step 4.17 Completion Message
# ============================================

print("\nValidation Completed")
print("Reports Created:")
print("validation_report.csv")
print("quality_test_report.csv")


