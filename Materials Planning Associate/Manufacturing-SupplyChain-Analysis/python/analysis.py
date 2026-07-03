import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load data
# -----------------------------
suppliers = pd.read_csv("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Materials Planning Associate\\Manufacturing-SupplyChain-Analysis\\data\\cleaned\\clean_suppliers.csv")
purchase_orders = pd.read_csv("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Materials Planning Associate\\Manufacturing-SupplyChain-Analysis\\data\\cleaned\\clean_purchase_orders.csv")
invoices = pd.read_csv("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Materials Planning Associate\\Manufacturing-SupplyChain-Analysis\\data\\cleaned\\clean_invoices.csv")
inventory = pd.read_csv("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Materials Planning Associate\\Manufacturing-SupplyChain-Analysis\\data\\cleaned\\clean_inventory.csv")
shipments = pd.read_csv("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Materials Planning Associate\\Manufacturing-SupplyChain-Analysis\\data\\cleaned\\clean_shipments.csv")

# Ensure date columns are parsed
purchase_orders["Order_Date"] = pd.to_datetime(purchase_orders["Order_Date"])
invoices["Invoice_Date"] = pd.to_datetime(invoices["Invoice_Date"])

# -----------------------------
# 2. KPIs
# -----------------------------

# Total Purchase Spend (PO_Amount)
total_purchase_spend = purchase_orders["PO_Amount"].sum()

# Average Lead Time (days)
avg_lead_time = suppliers["Lead_Time_Days"].mean()

# Late Shipment % (Delay_Days > 0)
late_shipments = shipments[shipments["Delay_Days"] > 0]
late_shipment_pct = len(late_shipments) / len(shipments) * 100

# Total Inventory Value
total_inventory_value = inventory["Inventory_Value"].sum()

# Pending Payments (sum of Final_Amount where Payment_Status = 'Pending')
pending_payments = invoices.loc[invoices["Payment_Status"] == "Pending", "Final_Amount"].sum()

# Average Supplier Rating
avg_supplier_rating = suppliers["Supplier_Rating"].mean()

# Invoice Difference (sum of discrepancies where Invoice_Discrepancy = True)
invoice_diff = invoices.loc[invoices["Invoice_Discrepancy"] == True, "Final_Amount"] - \
               invoices.loc[invoices["Invoice_Discrepancy"] == True, "Calculated_Total"]
total_invoice_diff = invoice_diff.sum()

# Top Suppliers (by PO_Amount)
po_by_supplier = purchase_orders.groupby("Supplier_ID")["PO_Amount"].sum().reset_index()
top_suppliers = po_by_supplier.sort_values("PO_Amount", ascending=False).head(10)

# Monthly Purchases (sum PO_Amount by month)
purchase_orders["PO_Month"] = purchase_orders["Order_Date"].dt.to_period("M")
monthly_purchases = purchase_orders.groupby("PO_Month")["PO_Amount"].sum().reset_index()

# Monthly Payments (sum Final_Amount by month)
invoices["Inv_Month"] = invoices["Invoice_Date"].dt.to_period("M")
monthly_payments = invoices.groupby("Inv_Month")["Final_Amount"].sum().reset_index()

# -----------------------------
# 3. Print KPIs
# -----------------------------
print("=== KPIs ===")
print(f"Total Purchase Spend: {total_purchase_spend:,.2f}")
print(f"Average Lead Time (days): {avg_lead_time:.2f}")
print(f"Late Shipment %: {late_shipment_pct:.2f}%")
print(f"Total Inventory Value: {total_inventory_value:,.2f}")
print(f"Pending Payments: {pending_payments:,.2f}")
print(f"Average Supplier Rating: {avg_supplier_rating:.2f}")
print(f"Total Invoice Difference (Final - Calculated, where True): {total_invoice_diff:,.2f}")
print("\nTop Suppliers by PO Amount:")
print(top_suppliers)

print("\nMonthly Purchases:")
print(monthly_purchases)

print("\nMonthly Payments:")
print(monthly_payments)

# -----------------------------
# 4. Charts
# -----------------------------
sns.set(style="whitegrid")

# 4.1 Bar Chart – Top Suppliers by PO Amount
plt.figure(figsize=(10, 5))
sns.barplot(data=top_suppliers, x="Supplier_ID", y="PO_Amount")
plt.title("Top Suppliers by Purchase Spend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4.2 Pie Chart – Purchase Spend by Category (from suppliers + POs)
po_suppliers = purchase_orders.merge(suppliers, on="Supplier_ID", how="left")
spend_by_category = po_suppliers.groupby("Category")["PO_Amount"].sum()
plt.figure(figsize=(6, 6))
plt.pie(spend_by_category, labels=spend_by_category.index, autopct="%1.1f%%")
plt.title("Purchase Spend by Supplier Category")
plt.show()

# 4.3 Scatter Plot – Lead Time vs Supplier Rating
plt.figure(figsize=(8, 5))
sns.scatterplot(data=suppliers, x="Lead_Time_Days", y="Supplier_Rating")
plt.title("Lead Time vs Supplier Rating")
plt.xlabel("Lead Time (days)")
plt.ylabel("Supplier Rating")
plt.tight_layout()
plt.show()

# 4.4 Line Chart – Monthly Purchases vs Monthly Payments
plt.figure(figsize=(10, 5))
plt.plot(monthly_purchases["PO_Month"].astype(str), monthly_purchases["PO_Amount"], label="Purchases")
plt.plot(monthly_payments["Inv_Month"].astype(str), monthly_payments["Final_Amount"], label="Payments")
plt.title("Monthly Purchases vs Monthly Payments")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 4.5 Heatmap – Inventory Stock by Warehouse and Material
pivot_inventory = inventory.pivot_table(index="Warehouse", columns="Material", values="Stock", aggfunc="sum")
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_inventory, cmap="Blues", annot=False)
plt.title("Inventory Stock Heatmap (Warehouse x Material)")
plt.tight_layout()
plt.show()

# 4.6 Histogram – Supplier Ratings
plt.figure(figsize=(8, 5))
sns.histplot(suppliers["Supplier_Rating"], bins=10, kde=True)
plt.title("Distribution of Supplier Ratings")
plt.xlabel("Rating")
plt.tight_layout()
plt.show()

# 4.7 Box Plot – Inventory Value by Warehouse
plt.figure(figsize=(8, 5))
sns.boxplot(data=inventory, x="Warehouse", y="Inventory_Value")
plt.title("Inventory Value Distribution by Warehouse")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
