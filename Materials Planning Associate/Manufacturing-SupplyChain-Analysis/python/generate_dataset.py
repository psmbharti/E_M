# 1. Import Libraries
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import timedelta

# 2. Create Faker Object
fake = Faker()

random.seed(42)
np.random.seed(42)  #Using a fixed seed ensures you get the same data every time, which is useful for testing.


 # 3. Create Lists for Random Data
countries = [
    "USA",
    "Canada",
    "Mexico",
    "Germany",
    "India",
    "China",
    "Japan",
    "South Korea"
]

categories = [
    "Electronics",
    "Mechanical",
    "Packaging",
    "Raw Materials",
    "Chemicals",
    "Plastic"
]

materials = [
    "Steel Rod",
    "Copper Wire",
    "Plastic Sheet",
    "Motor",
    "Circuit Board",
    "Sensor",
    "Bearing",
    "Aluminum Plate",
    "Rubber Seal",
    "Transformer"
]

warehouses = [
    "Dallas",
    "Chicago",
    "New York",
    "Atlanta",
    "Phoenix"
]

payment_status = [
    "Paid",
    "Pending",
    "Overdue"
]

shipment_status = [
    "Delivered",
    "Delayed",
    "In Transit"
]

order_status = [
    "Open",
    "Closed",
    "Cancelled"
]

# 4. Create the Suppliers Dataset
suppliers = []

for i in range(1, 51):

    suppliers.append({

        "Supplier_ID": f"SUP{i:03}",

        "Supplier_Name": fake.company(),

        "Country": random.choice(countries),

        "Category": random.choice(categories),

        "Lead_Time_Days": random.randint(3, 25),

        "Supplier_Rating": round(random.uniform(3.5, 5.0), 1)

    })

suppliers_df = pd.DataFrame(suppliers)

# Save Suppliers dataset to CSV
suppliers_df.to_csv(
    r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Materials Planning Associate\Manufacturing-SupplyChain-Analysis\data\suppliers.csv",
    index=False
)

print("Suppliers dataset created.")

# 5. Create Purchase Orders 
purchase_orders = []

for i in range(1, 201):

    supplier = random.choice(suppliers)

    quantity = random.randint(20, 500)

    price = random.randint(20, 500)

    order_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    expected_delivery = order_date + timedelta(
        days=random.randint(3, 20)
    )

    purchase_orders.append({

        "PO_Number": f"PO{i:04}",

        "Supplier_ID": supplier["Supplier_ID"],

        "Material": random.choice(materials),

        "Order_Date": order_date,

        "Expected_Delivery": expected_delivery,

        "Quantity": quantity,

        "Unit_Price": price,

        "PO_Amount": quantity * price,

        "Status": random.choice(order_status)

    })

purchase_df = pd.DataFrame(purchase_orders)

# Save Purchase Orders dataset to CSV
purchase_df.to_csv(
    r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Materials Planning Associate\Manufacturing-SupplyChain-Analysis\data\purchase_orders.csv",
    index=False
)

print("Purchase Orders created.")

# 6. Generate Invoices

invoices = []

for index, row in purchase_df.iterrows():

    invoice_amount = row["PO_Amount"]

    tax = round(invoice_amount * 0.08, 2)

    discount = random.choice([0, 50, 100, 150, 200])

    final_amount = invoice_amount + tax - discount

    # Introduce discrepancies in ~15% of invoices
    if random.random() < 0.15:
        final_amount += random.randint(-500, 500)

    invoices.append({

        "Invoice_ID": f"INV{index+1:04}",

        "PO_Number": row["PO_Number"],

        "Invoice_Date": row["Order_Date"] + timedelta(days=random.randint(1, 5)),

        "Invoice_Amount": invoice_amount,

        "Tax": tax,

        "Discount": discount,

        "Final_Amount": round(final_amount, 2),

        "Payment_Status": random.choice(payment_status)

    })

invoice_df = pd.DataFrame(invoices)

# Save the invoice dataset to CSV
invoice_df.to_csv(
    r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Materials Planning Associate\Manufacturing-SupplyChain-Analysis\data\invoices.csv",
    index=False
)
print("Invoices dataset created.")

# 7. Generate Inventory

inventory = []

for i in range(1, 201):

    material = random.choice(materials)

    stock = random.randint(20, 1000)

    reorder = random.randint(50, 200)

    inventory_value = stock * random.randint(10, 500)

    inventory.append({

        "Item_ID": f"ITM{i:04}",

        "Material": material,

        "Warehouse": random.choice(warehouses),

        "Stock": stock,

        "Reorder_Level": reorder,

        "Inventory_Value": inventory_value

    })

inventory_df = pd.DataFrame(inventory)

# Save the inventory dataset to CSV
inventory_df.to_csv(
    r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Materials Planning Associate\Manufacturing-SupplyChain-Analysis\data\inventory.csv",
    index=False
)

print("Inventory dataset created.")

# 8. Generate Shipments

shipments = []

for index, row in purchase_df.iterrows():

    dispatch = row["Order_Date"] + timedelta(days=1)

    actual_delivery = row["Expected_Delivery"] + timedelta(
        days=random.randint(-2, 8)
    )

    delay = (actual_delivery - row["Expected_Delivery"]).days

    shipments.append({

        "Shipment_ID": f"SHP{index+1:04}",

        "PO_Number": row["PO_Number"],

        "Dispatch_Date": dispatch,

        "Delivery_Date": actual_delivery,

        "Delay_Days": delay,

        "Shipment_Status": random.choice(shipment_status)

    })

shipment_df = pd.DataFrame(shipments)

# Save the shipment dataset to CSV
shipment_df.to_csv(
    r"C:\Users\madhu\OneDrive\Desktop\GITHUB_Resume_Projects\emp. magnet\Materials Planning Associate\Manufacturing-SupplyChain-Analysis\data\shipments.csv",
    index=False
)


print("Shipment dataset created.")
