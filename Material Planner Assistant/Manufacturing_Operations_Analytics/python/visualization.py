# Step 1: Import Libraries

import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load Datasets
manufacturing = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Material Planner Assistant\Manufacturing_Operations_Analytics\dataset\manufacturing_orders.csv")
purchase = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Material Planner Assistant\Manufacturing_Operations_Analytics\dataset\purchase_orders.csv")
sales = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Material Planner Assistant\Manufacturing_Operations_Analytics\dataset\sales_orders.csv")
invoice = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Material Planner Assistant\Manufacturing_Operations_Analytics\dataset\vendor_invoices.csv")

# Step 3: Convert Date Columns to Datetime
manufacturing["Order_Date"] = pd.to_datetime(manufacturing["Order_Date"])
manufacturing["Month"] = manufacturing["Order_Date"].dt.strftime("%b")

# Chart 1: Production Status
status = manufacturing["Production_Status"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(status,
        labels=status.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Production Status")
plt.savefig("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\charts\\production_status.png")
plt.show()

# Chart 2: Monthly Orders
monthly = manufacturing.groupby("Month")["Order_ID"].count()

plt.figure(figsize=(10,5))
plt.plot(monthly.index,
         monthly.values,
         marker="o")

plt.title("Monthly Manufacturing Orders")
plt.xlabel("Month")
plt.ylabel("Orders")

plt.grid(True)

plt.savefig("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\charts\\monthly_orders.png")

plt.show()

# Chart 3: Supplier Spend
supplier = purchase.groupby("Supplier")["PO_Amount"].sum()

plt.figure(figsize=(10,6))

plt.bar(supplier.index,
        supplier.values)

plt.xticks(rotation=45)

plt.title("Supplier Spend")

plt.xlabel("Supplier")

plt.ylabel("Purchase Amount")

plt.tight_layout()

plt.savefig("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\charts\\supplier_spend.png")

plt.show()

# Chart 4: Forecast vs Actual
forecast = manufacturing.groupby("Product_Name")[["Forecast_Qty","Actual_Qty"]].sum()

forecast.plot(kind="bar",
              figsize=(12,6))

plt.title("Forecast vs Actual Production")

plt.ylabel("Quantity")

plt.tight_layout()

plt.savefig("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\charts\\forecast_vs_actual.png")

plt.show()

# Chart 5: Work Center Load
work = manufacturing["Work_Center"].value_counts()

plt.figure(figsize=(8,5))

plt.bar(work.index,
        work.values)

plt.title("Work Center Load")

plt.xlabel("Work Center")

plt.ylabel("Orders")

plt.savefig("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\charts\\work_center_load.png")

plt.show()

# Chart 6: Order Priority
priority = manufacturing["Production_Priority"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(priority,
        labels=priority.index,
        autopct="%1.1f%%")

plt.title("Production Priority")

plt.savefig("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\charts\\order_priority.png")

plt.show()

# Chart 7: Invoice Validation
validation = invoice["Validation_Status"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(validation,
        labels=validation.index,
        autopct="%1.1f%%")

plt.title("Invoice Validation")

plt.savefig("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\charts\\invoice_validation.png")

plt.show()

