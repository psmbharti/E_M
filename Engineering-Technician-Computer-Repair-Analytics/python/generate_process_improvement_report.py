import os
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

df = pd.read_csv("data/computer_repairs_clean.csv")
os.makedirs("reports", exist_ok=True)

doc = SimpleDocTemplate("reports/Process_Improvement_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

header_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#003366")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
])

def add_table(title, df_section):
    elements.append(Paragraph(title, styles["Heading2"]))
    elements.append(Spacer(1, 10))
    table_data = [df_section.columns.tolist()] + df_section.values.tolist()
    table = Table(table_data)
    table.setStyle(header_style)
    elements.append(table)
    elements.append(Spacer(1, 20))

def add_chart(title, fig_path):
    elements.append(Paragraph(title, styles["Heading2"]))
    elements.append(Spacer(1, 10))
    elements.append(Image(fig_path, width=400, height=250))
    elements.append(Spacer(1, 20))

# MTTR Chart
plt.figure(figsize=(6,4))
plt.hist(df["Repair_Time_Hours"], bins=10, color="#003366")
plt.title("Repair Time Distribution (MTTR)")
plt.tight_layout()
mttr_chart = "Screenshot/mttr_chart.png"
plt.savefig(mttr_chart)
plt.close()

time_df = pd.DataFrame({
    "Metric": ["MTTR", "Median Repair Time"],
    "Hours": [df["Repair_Time_Hours"].mean(), df["Repair_Time_Hours"].median()]
})
add_table("Repair Time Metrics", time_df)
add_chart("Repair Time Chart", mttr_chart)

# Cost per Category Chart
cost_cat = df.groupby("Failure_Category")["Repair_Cost"].mean()
plt.figure(figsize=(6,4))
cost_cat.plot(kind="bar", color="#003366")
plt.title("Cost per Category")
plt.tight_layout()
cost_chart = "Screenshot/cost_chart.png"
plt.savefig(cost_chart)
plt.close()

cost_df = cost_cat.reset_index()
cost_df.columns = ["Failure Category", "Avg Cost"]
add_table("Cost per Category", cost_df)
add_chart("Cost per Category Chart", cost_chart)

# Warehouse Performance Chart
warehouse = df.groupby("Warehouse")["Repair_ID"].count()
plt.figure(figsize=(6,4))
warehouse.plot(kind="bar", color="#003366")
plt.title("Warehouse Performance")
plt.tight_layout()
warehouse_chart = "Screenshot/warehouse_chart.png"
plt.savefig(warehouse_chart)
plt.close()

warehouse_df = warehouse.reset_index()
warehouse_df.columns = ["Warehouse", "Repairs"]
add_table("Warehouse Performance", warehouse_df)
add_chart("Warehouse Performance Chart", warehouse_chart)

# Supplier Reliability Chart
supplier = df.groupby("Supplier")["Customer_Satisfaction"].mean()
plt.figure(figsize=(6,4))
supplier.plot(kind="bar", color="#003366")
plt.title("Supplier Reliability (Avg Satisfaction)")
plt.tight_layout()
supplier_chart = "Screenshot/supplier_chart.png"
plt.savefig(supplier_chart)
plt.close()

supplier_df = supplier.reset_index()
supplier_df.columns = ["Supplier", "Avg Satisfaction"]
add_table("Supplier Reliability Metrics", supplier_df)
add_chart("Supplier Reliability Chart", supplier_chart)

doc.build(elements)
print("Process_Improvement_Report.pdf created with charts.")
