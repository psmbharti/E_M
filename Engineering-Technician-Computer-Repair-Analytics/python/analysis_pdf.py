import os
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Load dataset
df = pd.read_csv("data\computer_repairs_clean.csv")

# Create reports folder
os.makedirs("reports", exist_ok=True)

# PDF setup
pdf_path = "reports/Repair_Analytics_Tables.pdf"
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
section_style = styles["Heading2"]
body_style = styles["BodyText"]

doc = SimpleDocTemplate(pdf_path, pagesize=A4)
elements = []

# Table header style
header_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#003366")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
])

# Helper to add table sections
def add_table(title, df_section):
    elements.append(Paragraph(title, section_style))
    elements.append(Spacer(1, 10))

    table_data = [df_section.columns.tolist()] + df_section.values.tolist()
    table = Table(table_data)
    table.setStyle(header_style)
    elements.append(table)
    elements.append(Spacer(1, 20))


# -----------------------------
# Generate all analytics tables
# -----------------------------

# 1. Total Repairs
total_repairs_df = pd.DataFrame({"Total Repairs": [len(df)]})
add_table("Total Repairs Completed", total_repairs_df)

# 2. Failure Rate
failure_rate_df = df['Failure_Category'].value_counts(normalize=True).mul(100).reset_index()
failure_rate_df.columns = ["Failure Category", "Failure Rate (%)"]
add_table("Failure Rate", failure_rate_df)

# 3. Average & Median Repair Time
time_df = pd.DataFrame({
    "Metric": ["Average Repair Time", "Median Repair Time"],
    "Hours": [df['Repair_Time_Hours'].mean(), df['Repair_Time_Hours'].median()]
})
add_table("Repair Time Metrics", time_df)

# 4. Most Common Repair Categories
common_cat_df = df['Failure_Category'].value_counts().reset_index()
common_cat_df.columns = ["Failure Category", "Count"]
add_table("Most Common Repair Categories", common_cat_df)

# 5. Technician Productivity
tech_prod_df = df.groupby("Engineer").agg(
    Repairs=("Repair_ID", "count"),
    Avg_Time=("Repair_Time_Hours", "mean"),
    Avg_Satisfaction=("Customer_Satisfaction", "mean")
).reset_index()
add_table("Technician Productivity", tech_prod_df)

# 6. QC Pass vs Fail
qc_df = df['QC_Status'].value_counts().reset_index()
qc_df.columns = ["QC Status", "Count"]
add_table("QC Pass vs Fail", qc_df)

# 7. Cost per Category
cost_cat_df = df.groupby("Failure_Category")['Repair_Cost'].mean().reset_index()
cost_cat_df.columns = ["Failure Category", "Avg Cost"]
add_table("Cost per Category", cost_cat_df)

# 8. Rework Rate
rework_df = df['Rework'].value_counts(normalize=True).mul(100).reset_index()
rework_df.columns = ["Rework Status", "Rate (%)"]
add_table("Rework Rate", rework_df)

# 9. QC Distribution
qc_dist_df = df['QC_Status'].value_counts(normalize=True).mul(100).reset_index()
qc_dist_df.columns = ["QC Status", "Distribution (%)"]
add_table("QC Distribution", qc_dist_df)

# 10. Satisfaction Summary
sat_df = df['Customer_Satisfaction'].describe().reset_index()
sat_df.columns = ["Statistic", "Value"]
add_table("Customer Satisfaction Summary", sat_df)

# 11. Warehouse Performance
warehouse_df = df.groupby("Warehouse").agg(
    Repairs=("Repair_ID", "count"),
    Avg_Time=("Repair_Time_Hours", "mean"),
    Avg_Cost=("Repair_Cost", "mean")
).reset_index()
add_table("Warehouse Performance", warehouse_df)

# 12. Supplier Reliability
supplier_df = df.groupby("Supplier").agg(
    Repairs=("Repair_ID", "count"),
    Avg_Satisfaction=("Customer_Satisfaction", "mean"),
    Avg_Cost=("Repair_Cost", "mean")
).reset_index()
add_table("Supplier Reliability Metrics", supplier_df)

# Build PDF
doc.build(elements)

print("PDF created successfully:", pdf_path)
