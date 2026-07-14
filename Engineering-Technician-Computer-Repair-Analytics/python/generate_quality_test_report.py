import os
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

df = pd.read_csv("data/computer_repairs_clean.csv")
os.makedirs("reports", exist_ok=True)

doc = SimpleDocTemplate("reports/Quality_Test_Report.pdf", pagesize=A4)
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

# QC Pass vs Fail Chart
qc_counts = df["QC_Status"].value_counts()
plt.figure(figsize=(6,4))
qc_counts.plot(kind="bar", color="#003366")
plt.title("QC Pass vs Fail")
plt.tight_layout()
qc_chart = "Screenshot/qc_chart.png"
plt.savefig(qc_chart)
plt.close()

qc_df = qc_counts.reset_index()
qc_df.columns = ["QC Status", "Count"]
add_table("QC Pass vs Fail", qc_df)
add_chart("QC Pass vs Fail Chart", qc_chart)

# Rework Rate Chart
rework = df["Rework"].value_counts()
plt.figure(figsize=(6,4))
rework.plot(kind="pie", autopct="%1.1f%%", colors=["#003366", "#6699CC"])
plt.title("Rework Rate")
plt.tight_layout()
rework_chart = "Screenshot/rework_chart.png"
plt.savefig(rework_chart)
plt.close()

rework_df = rework.reset_index()
rework_df.columns = ["Rework Status", "Count"]
add_table("Rework Rate", rework_df)
add_chart("Rework Rate Chart", rework_chart)

# Satisfaction Chart
plt.figure(figsize=(7,4))
df["Customer_Satisfaction"].plot(kind="hist", bins=5, color="#003366")
plt.title("Customer Satisfaction Distribution")
plt.tight_layout()
sat_chart = "Screenshot/satisfaction_chart.png"
plt.savefig(sat_chart)
plt.close()

sat_df = df["Customer_Satisfaction"].describe().reset_index()
sat_df.columns = ["Statistic", "Value"]
add_table("Customer Satisfaction Summary", sat_df)
add_chart("Customer Satisfaction Chart", sat_chart)

# Failure Category Chart
fail_cat = df["Failure_Category"].value_counts()
plt.figure(figsize=(6,4))
fail_cat.plot(kind="bar", color="#003366")
plt.title("Failure Categories")
plt.tight_layout()
fail_chart = "Screenshot/failure_chart.png"
plt.savefig(fail_chart)
plt.close()

fail_df = fail_cat.reset_index()
fail_df.columns = ["Failure Category", "Count"]
add_table("Failure Categories", fail_df)
add_chart("Failure Categories Chart", fail_chart)

doc.build(elements)
print("Quality_Test_Report.pdf created with charts.")
