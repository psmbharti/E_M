import os
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

df = pd.read_csv("data\computer_repairs_clean.csv")
os.makedirs("reports", exist_ok=True)

doc = SimpleDocTemplate("reports/Engineering_Report.pdf", pagesize=A4)
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


# Device Type Performance Chart
device_perf = df.groupby("Device_Type")["Repair_ID"].count()
plt.figure(figsize=(6,4))
device_perf.plot(kind="bar", color="#003366")
plt.title("Device Type Performance")
plt.tight_layout()
device_chart = "Screenshot/device_chart.png"
plt.savefig(device_chart)
plt.close()

device_df = device_perf.reset_index()
device_df.columns = ["Device Type", "Repairs"]
add_table("Device Type Performance", device_df)
add_chart("Device Type Performance Chart", device_chart)

# Failure Type Chart
fail_type = df["Failure_Type"].value_counts()
plt.figure(figsize=(6,4))
fail_type.plot(kind="bar", color="#003366")
plt.title("Failure Types")
plt.tight_layout()
failtype_chart = "Screenshot/failuretype_chart.png"
plt.savefig(failtype_chart)
plt.close()

failtype_df = fail_type.reset_index()
failtype_df.columns = ["Failure Type", "Count"]
add_table("Failure Types", failtype_df)
add_chart("Failure Types Chart", failtype_chart)




doc.build(elements)
print("Engineering_Report.pdf created with charts.")
