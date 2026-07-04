# ============================================================
#   MATERIAL PLANNER — COMPLETE PYTHON CLEANING PIPELINE
# ============================================================

import pandas as pd
import numpy as np

# ------------------------------------------------------------
# Load Datasets
# ------------------------------------------------------------

manufacturing = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Material Planner Assistant\Manufacturing_Operations_Analytics\dataset\Manufacturing_Orders.csv")
purchase = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Material Planner Assistant\Manufacturing_Operations_Analytics\dataset\Purchase_Orders.csv")
sales = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Material Planner Assistant\Manufacturing_Operations_Analytics\dataset\Sales_Orders.csv")
invoice = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Material Planner Assistant\Manufacturing_Operations_Analytics\dataset\Vendor_Invoices.csv")

# ------------------------------------------------------------
# Missing Values Check
# ------------------------------------------------------------

print("=== Missing Values Before Cleaning ===")
print(manufacturing.isnull().sum())
print(purchase.isnull().sum())
print(sales.isnull().sum())
print(invoice.isnull().sum())

# ------------------------------------------------------------
# Remove Duplicates
# ------------------------------------------------------------

for df in [manufacturing, purchase, sales, invoice]:
    df.drop_duplicates(inplace=True)

# ------------------------------------------------------------
# Convert Date Columns
# ------------------------------------------------------------

date_columns = [
    (manufacturing, ["Order_Date", "Due_Date"]),
    (purchase, ["PO_Date"]),
    (sales, ["Sales_Date"]),
    (invoice, ["Invoice_Date"])
]

for df, cols in date_columns:
    for col in cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# ------------------------------------------------------------
# Validate Quantity Fields
# ------------------------------------------------------------

# Manufacturing
manufacturing["Quantity"] = manufacturing["Quantity"].abs()
manufacturing["Completed_Qty"] = manufacturing["Completed_Qty"].clip(lower=0)

# Purchase
purchase["Ordered_Qty"] = purchase["Ordered_Qty"].abs()
purchase["Received_Qty"] = purchase["Received_Qty"].clip(lower=0)

# Sales
sales["Order_Qty"] = sales["Order_Qty"].abs()

# ------------------------------------------------------------
# Recalculate Business Rules
# ------------------------------------------------------------

# Pending Quantity
manufacturing["Pending_Qty"] = (
    manufacturing["Quantity"] - manufacturing["Completed_Qty"]
).clip(lower=0)

# Forecast Error
manufacturing["Forecast_Error"] = (
    manufacturing["Actual_Qty"] - manufacturing["Forecast_Qty"]
)

# ------------------------------------------------------------
# Merge PO Amount into Invoice Dataset
# ------------------------------------------------------------

invoice = invoice.merge(
    purchase[["PO_Number", "PO_Amount"]],
    on="PO_Number",
    how="left"
)

# Recalculate Invoice Difference
invoice["Difference"] = invoice["Invoice_Amount"] - invoice["PO_Amount"]

# ------------------------------------------------------------
# Invoice Validation Rule
# ------------------------------------------------------------

def validate_invoice(diff):
    return "Valid" if abs(diff) <= 50 else "Mismatch"

invoice["Validation"] = invoice["Difference"].apply(validate_invoice)

# Finance Status Cleanup
invoice["Finance_Status"] = invoice["Finance_Status"].fillna("Pending")

# ------------------------------------------------------------
# Remove Invalid Rows
# ------------------------------------------------------------

manufacturing = manufacturing[manufacturing["Quantity"] > 0]
purchase = purchase[purchase["Ordered_Qty"] > 0]
sales = sales[sales["Order_Qty"] > 0]

# ------------------------------------------------------------
# Handle Missing Values
# ------------------------------------------------------------

for df in [manufacturing, purchase, sales, invoice]:
    df.fillna("Unknown", inplace=True)

# ------------------------------------------------------------
# Standardize Text Columns
# ------------------------------------------------------------

manufacturing["Production_Status"] = manufacturing["Production_Status"].str.title()
purchase["PO_Status"] = purchase["PO_Status"].str.title()
sales["Status"] = sales["Status"].str.title()
invoice["Validation"] = invoice["Validation"].str.title()

# ------------------------------------------------------------
# Final Data Quality Summary
# ------------------------------------------------------------

print("\n=== After Cleaning ===")
print(manufacturing.info())
print(purchase.info())
print(sales.info())
print(invoice.info())

print("\n=== Cleaning Complete ===")
print(f"Manufacturing Records : {len(manufacturing)}")
print(f"Purchase Records      : {len(purchase)}")
print(f"Sales Records         : {len(sales)}")
print(f"Invoice Records       : {len(invoice)}")

