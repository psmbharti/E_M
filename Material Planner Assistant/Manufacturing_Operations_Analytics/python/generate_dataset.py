import pandas as pd
import random
from faker import Faker
from datetime import timedelta

fake = Faker()

NUM_RECORDS = 500

products = [
    "Steel Cabinet", "Metal Shelf", "Office Chair", "Wooden Table",
    "Storage Rack", "Tool Box", "Filing Cabinet", "Computer Desk",
    "Workbench", "Locker"
]

suppliers = [
    "ABC Metals", "Global Steel", "Prime Industries", "United Supplies",
    "Industrial Parts", "Blue Manufacturing", "Rapid Components",
    "Future Materials", "Titan Supply", "Vertex Industries"
]

customers = [
    "Amazon", "Tesla", "Dell", "HP", "Samsung", "Apple",
    "Target", "Walmart", "Costco", "Best Buy"
]

operations = ["Cutting", "Welding", "Painting", "Assembly", "Quality Control"]
work_centers = ["Line A", "Line B", "Line C", "Line D"]
statuses = ["Completed", "In Progress", "Delayed"]
planners = ["John", "David", "Emily", "Sophia", "Michael"]
buyers = ["Alice", "Robert", "James", "Linda", "Daniel"]

manufacturing_data = []
purchase_data = []
sales_data = []
invoice_data = []

# ---------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------
for i in range(1, NUM_RECORDS + 1):

    # IDs
    order_id = f"ORD{i:04}"
    mo = f"MO{i:04}"
    tt = f"TT{i:04}"
    product_id = f"P{i:03}"

    # Random selections
    product = random.choice(products)
    customer = random.choice(customers)

    # Dates
    order_date = fake.date_between(start_date="-1y", end_date="today")
    due_date = order_date + timedelta(days=random.randint(3, 20))

    # Manufacturing fields
    operation = random.choice(operations)
    work_center = random.choice(work_centers)
    priority = random.choice(["High", "Medium", "Low"])

    quantity = random.randint(50, 500)
    completed_quantity = random.randint(0, quantity)
    pending_quantity = quantity - completed_quantity

    status = random.choice(statuses)
    planner = random.choice(planners)

    forecast = random.randint(50, 500)
    actual = random.randint(50, 500)
    forecast_error = actual - forecast

    # Append manufacturing record
    manufacturing_data.append({
        "Order_ID": order_id,
        "Product_ID": product_id,
        "Product_Name": product,
        "Customer": customer,
        "Order_Date": order_date,
        "Due_Date": due_date,
        "Manufacturing_Order": mo,
        "Transfer_Ticket": tt,
        "Operation": operation,
        "Work_Center": work_center,
        "Production_Priority": priority,
        "Quantity": quantity,
        "Completed_Qty": completed_quantity,
        "Pending_Qty": pending_quantity,
        "Production_Status": status,
        "Production_Control": planner,
        "Forecast_Qty": forecast,
        "Actual_Qty": actual,
        "Forecast_Error": forecast_error
    })

    # Purchase Order
    po_number = f"PO{i:04}"
    supplier = random.choice(suppliers)
    ordered_qty = quantity
    received_qty = random.randint(0, ordered_qty)
    po_amount = ordered_qty * random.randint(20, 120)
    buyer = random.choice(buyers)
    po_status = random.choice(["Open", "Closed", "Partial"])

    purchase_data.append({
        "PO_Number": po_number,
        "Supplier": supplier,
        "PO_Date": order_date,
        "Item": product,
        "Ordered_Qty": ordered_qty,
        "Received_Qty": received_qty,
        "PO_Amount": po_amount,
        "Buyer": buyer,
        "PO_Status": po_status
    })

    # Sales Order
    so_number = f"SO{i:04}"
    order_qty = quantity
    sales_amount = order_qty * random.randint(80, 250)
    sales_status = random.choice(["Open", "Completed", "Cancelled"])

    sales_data.append({
        "SO_Number": so_number,
        "Customer": customer,
        "Sales_Date": order_date,
        "Product": product,
        "Order_Qty": order_qty,
        "Sales_Amount": sales_amount,
        "Status": sales_status
    })

    # Invoice
    invoice_id = f"INV{i:04}"
    difference = random.randint(50, 500)
    invoice_amount = po_amount + difference

    validation = "Valid" if abs(difference) <= 50 else "Mismatch"
    finance_status = random.choice(["Approved", "Pending", "On Hold"])

  
    invoice_data.append({
    "Invoice_ID": invoice_id,
    "Supplier": supplier,
    "Invoice_Date": due_date,
    "PO_Number": po_number,
    "Invoice_Amount": invoice_amount,
    "PO_Amount": po_amount,
    "Difference": difference,
    "Validation_Status": validation,
    "Finance_Status": finance_status
})
    

# ---------------------------------------------------------
# Convert to DataFrames
# ---------------------------------------------------------
manufacturing_df = pd.DataFrame(manufacturing_data)
purchase_df = pd.DataFrame(purchase_data)
sales_df = pd.DataFrame(sales_data)
invoice_df = pd.DataFrame(invoice_data)



# ---------------------------------------------------------
# Save CSVs
# ---------------------------------------------------------
manufacturing_df.to_csv("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\dataset\\manufacturing_orders.csv", index=False)
purchase_df.to_csv("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\dataset\\purchase_orders.csv", index=False)
sales_df.to_csv("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\dataset\\sales_orders.csv", index=False)
invoice_df.to_csv("C:\\Users\\madhu\\OneDrive\\Desktop\\GITHUB_Resume_Projects\\emp. magnet\\Material Planner Assistant\\Manufacturing_Operations_Analytics\\dataset\\vendor_invoices.csv", index=False
) 
print("=" * 50)
print("Manufacturing datasets generated successfully!")
print("=" * 50)

print(f"Manufacturing Orders : {len(manufacturing_df)}")
print(f"Purchase Orders      : {len(purchase_df)}")
print(f"Sales Orders         : {len(sales_df)}")
print(f"Vendor Invoices      : {len(invoice_df)}")

