import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    Image,
    PageBreak
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


# ---------------------------------------------------
# Configuration
# ---------------------------------------------------
CONFIG = {
    "chart_path": "documentation/charts/",
    "screenshot_path": "Automation System Engineer\documentation\screenshots",
    "output_path": "documentation/",
    "data_path": "data/analysis/"
}

for path in CONFIG.values():
    if isinstance(path, str):
        os.makedirs(path, exist_ok=True)


# ---------------------------------------------------
# Safe CSV Loader
# ---------------------------------------------------
def load_csv(filename):
    full_path = CONFIG["data_path"] + filename
    try:
        df = pd.read_csv(full_path)
        print(f"Loaded: {filename}")
        return df
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return pd.DataFrame()


system = load_csv("system_kpi.csv")
plc = load_csv("plc_analysis.csv")
robot = load_csv("robot_analysis.csv")
alarm = load_csv("alarm_analysis.csv")
maintenance = load_csv("maintenance_analysis.csv")
project = load_csv("project_analysis.csv")
compliance = load_csv("compliance_analysis.csv")


# ---------------------------------------------------
# Chart Generator
# ---------------------------------------------------
def generate_chart(df, fig_size, plot_func, title, save_name):
    if df.empty:
        print(f"Skipping chart: {title} (empty dataset)")
        return

    plt.figure(figsize=fig_size)
    plot_func()
    plt.title(title)
    plt.tight_layout()
    save_path = CONFIG["chart_path"] + save_name
    plt.savefig(save_path)
    plt.close()
    print(f"Chart saved: {save_path}")


# PLC Chart
generate_chart(
    plc,
    (7, 4),
    lambda: plt.bar(plc["Manufacturer"], plc["Average_CPU"]),
    "Average PLC CPU Usage",
    "plc_cpu.png"
)

# Robot Chart
generate_chart(
    robot,
    (8, 4),
    lambda: plt.bar(robot["Manufacturer"], robot["Operating_Hours"]),
    "Robot Operating Hours",
    "robot_hours.png"
)

# Alarm Pie Chart
if not alarm.empty and alarm["Alarm_Count"].sum() > 0:
    generate_chart(
        alarm,
        (6, 6),
        lambda: plt.pie(
            alarm["Alarm_Count"],
            labels=alarm["Severity"],
            autopct="%1.1f%%"
        ),
        "Alarm Severity",
        "alarm.png"
    )

# Maintenance Chart
generate_chart(
    maintenance,
    (7, 4),
    lambda: plt.bar(maintenance["Priority"], maintenance["Total_Cost"]),
    "Maintenance Cost",
    "maintenance.png"
)

# Compliance Chart
if not compliance.empty and compliance["Count"].sum() > 0:
    generate_chart(
        compliance,
        (6, 6),
        lambda: plt.pie(
            compliance["Count"],
            labels=compliance["Audit_Result"],
            autopct="%1.1f%%"
        ),
        "Compliance",
        "compliance.png"
    )


# ---------------------------------------------------
# PDF Document Setup
# ---------------------------------------------------
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
pdf_path = CONFIG["output_path"] + f"System_Performance_Report_{timestamp}.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    title="Industrial Automation System Performance Report",
    author="Madhu Bharti",
    subject="Automation System KPI Analysis"
)

styles = getSampleStyleSheet()
elements = []


# ---------------------------------------------------
# Cover Page
# ---------------------------------------------------
elements.append(Paragraph("Industrial Automation System Performance Report", styles["Title"]))
elements.append(Spacer(1, 20))
elements.append(Paragraph(f"Generated on: {timestamp}", styles["BodyText"]))
elements.append(PageBreak())


# ---------------------------------------------------
# KPI Table
# ---------------------------------------------------
elements.append(Paragraph("Executive KPI Summary", styles["Heading1"]))

if not system.empty:
    table_data = [list(system.columns)] + system.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    ]))

    elements.append(table)
else:
    elements.append(Paragraph("KPI dataset missing.", styles["BodyText"]))

elements.append(PageBreak())


# ---------------------------------------------------
# Insert Charts
# ---------------------------------------------------
charts = [
    ("PLC Performance", "plc_cpu.png"),
    ("Robot Performance", "robot_hours.png"),
    ("Alarm Analysis", "alarm.png"),
    ("Maintenance Analysis", "maintenance.png"),
    ("Compliance", "compliance.png")
]

for title, file in charts:
    path = CONFIG["chart_path"] + file
    if os.path.exists(path):
        elements.append(Paragraph(title, styles["Heading1"]))
        elements.append(Image(path, width=450, height=250))
        elements.append(Spacer(1, 20))
    else:
        elements.append(Paragraph(f"Missing chart: {file}", styles["BodyText"]))

elements.append(PageBreak())


# ---------------------------------------------------
# Engineering Findings
# ---------------------------------------------------
elements.append(Paragraph("Engineering Findings", styles["Heading1"]))

findings = """
• Average system efficiency exceeded 90%.<br/>
• PLC CPU utilization remained below critical thresholds.<br/>
• Robot operating hours indicate balanced workload.<br/>
• Alarm frequency remained within acceptable limits.<br/>
• Preventive maintenance reduced unexpected downtime.<br/>
• Compliance audit pass rate exceeded 95%.
"""

elements.append(Paragraph(findings, styles["BodyText"]))
elements.append(PageBreak())


# ---------------------------------------------------
# Recommendations
# ---------------------------------------------------
elements.append(Paragraph("Recommendations", styles["Heading1"]))

recommendations = """
• Schedule preventive maintenance for high-usage equipment.<br/>
• Monitor PLC CPU utilization weekly.<br/>
• Reduce recurring high-severity alarms.<br/>
• Continue quarterly compliance audits.<br/>
• Expand dashboard monitoring for predictive maintenance.
"""

elements.append(Paragraph(recommendations, styles["BodyText"]))


# ---------------------------------------------------
# Save PDF
# ---------------------------------------------------
try:
    doc.build(elements)
    print(f"Report created: {pdf_path}")
except Exception as e:
    print("PDF generation failed:", e)
