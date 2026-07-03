
# Import Libraries
import pandas as pd
import os

# Define File Paths
# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

OUTPUT_DIR = os.path.join(DATA_DIR, "cleaned")

# Create cleaned folder automatically
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Load All CSV Files
suppliers = pd.read_csv(os.path.join(DATA_DIR, "suppliers.csv"))

purchase_orders = pd.read_csv(os.path.join(DATA_DIR, "purchase_orders.csv"))

invoices = pd.read_csv(os.path.join(DATA_DIR, "invoices.csv"))

inventory = pd.read_csv(os.path.join(DATA_DIR, "inventory.csv"))

shipments = pd.read_csv(os.path.join(DATA_DIR, "shipments.csv"))

# Display Dataset Information

# print("\nDataset Shapes")

# print("-------------------------")

# print("Suppliers :", suppliers.shape)

# print("Purchase Orders :", purchase_orders.shape)

# print("Invoices :", invoices.shape)

# print("Inventory :", inventory.shape)

# print("Shipments :", shipments.shape)

# Remove Duplicate Records
suppliers = suppliers.drop_duplicates()

purchase_orders = purchase_orders.drop_duplicates()

invoices = invoices.drop_duplicates()

inventory = inventory.drop_duplicates()

shipments = shipments.drop_duplicates()

# print("\nDuplicate records removed.")

# Check missing values first:
# print("\nMissing Values")

# print("-------------------------")

# print(suppliers.isnull().sum())

# print(purchase_orders.isnull().sum())

# print(invoices.isnull().sum())

# print(inventory.isnull().sum())

# print(shipments.isnull().sum())

# Fill missing values with appropriate strategies
suppliers.fillna("Unknown", inplace=True)

purchase_orders.fillna(0, inplace=True)

invoices.fillna(0, inplace=True)

inventory.fillna(0, inplace=True)

shipments.fillna(0, inplace=True)

# print("\nMissing values handled.")

# Standardize Date Formats

purchase_orders["Order_Date"] = pd.to_datetime(
    purchase_orders["Order_Date"]
)

purchase_orders["Expected_Delivery"] = pd.to_datetime(
    purchase_orders["Expected_Delivery"]
)

invoices["Invoice_Date"] = pd.to_datetime(
    invoices["Invoice_Date"]
)

shipments["Dispatch_Date"] = pd.to_datetime(
    shipments["Dispatch_Date"]
)

shipments["Delivery_Date"] = pd.to_datetime(
    shipments["Delivery_Date"]
)

# print("\nDates standardized.")

# Validate Invoice Totals
invoices["Calculated_Total"] = (
    invoices["Invoice_Amount"]
    + invoices["Tax"]
    - invoices["Discount"]
)
# Flag Invoice Discrepancies
invoices["Invoice_Discrepancy"] = (
    invoices["Final_Amount"]
    != invoices["Calculated_Total"]
)

print("\nInvoice discrepancies detected:",
      invoices["Invoice_Discrepancy"].sum())

# Identify Low-Stock Inventory
inventory["Low_Stock"] = (
    inventory["Stock"]
    < inventory["Reorder_Level"]
)

print("\nLow stock items:",
      inventory["Low_Stock"].sum())

# Check for Negative Values
purchase_orders["Quantity"] = purchase_orders["Quantity"].clip(lower=0)

purchase_orders["Unit_Price"] = purchase_orders["Unit_Price"].clip(lower=0)

purchase_orders["PO_Amount"] = purchase_orders["PO_Amount"].clip(lower=0)

inventory["Stock"] = inventory["Stock"].clip(lower=0)

inventory["Inventory_Value"] = inventory["Inventory_Value"].clip(lower=0)

# Standardize Text Columns
suppliers["Supplier_Name"] = (
    suppliers["Supplier_Name"]
    .str.strip()
    .str.title()
)

suppliers["Country"] = (
    suppliers["Country"]
    .str.strip()
    .str.title()
)

suppliers["Category"] = (
    suppliers["Category"]
    .str.strip()
    .str.title()
)
# Save Cleaned Files
suppliers.to_csv(
    os.path.join(OUTPUT_DIR, "clean_suppliers.csv"),
    index=False
)

purchase_orders.to_csv(
    os.path.join(OUTPUT_DIR, "clean_purchase_orders.csv"),
    index=False
)

invoices.to_csv(
    os.path.join(OUTPUT_DIR, "clean_invoices.csv"),
    index=False
)

inventory.to_csv(
    os.path.join(OUTPUT_DIR, "clean_inventory.csv"),
    index=False
)

shipments.to_csv(
    os.path.join(OUTPUT_DIR, "clean_shipments.csv"),
    index=False
)

# Print Summary Report
print("\nCleaning Summary")
print("-------------------------")

print("Suppliers :", len(suppliers))

print("Purchase Orders :", len(purchase_orders))

print("Invoices :", len(invoices))

print("Inventory :", len(inventory))

print("Shipments :", len(shipments))

print("Invoice Discrepancies :",
      invoices["Invoice_Discrepancy"].sum())

print("Low Stock Items :",
      inventory["Low_Stock"].sum())

print("\nAll cleaned datasets saved successfully!")