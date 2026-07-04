📦 Manufacturing Operations \& Supply Chain Analytics Dashboard

📊 Project Overview



This project simulates a real-world manufacturing and supply chain analytics system used in production and operations management.



It covers the complete data pipeline:



Data Generation (Python)

Data Cleaning \& Validation

SQL Database Modeling

KPI Analysis

Python Data Visualization



The goal is to analyze manufacturing efficiency, supplier performance, production delays, invoice validation, and sales trends.



🧰 Tools \& Technologies

Python (Pandas, Faker, Matplotlib)

SQL (MySQL Workbench)

Microsoft Excel



GitHub

📁 Project Structure

Manufacturing\_Operations\_Analytics/



│

├── dataset/

│   ├── manufacturing\_orders.csv

│   ├── purchase\_orders.csv

│   ├── sales\_orders.csv

│   ├── vendor\_invoices.csv

│   └

│

├── python/

│   ├── generate\_dataset.py

│   ├── clean\_data.py

│   └── visualization.py

│

├── sql/

│   ├── create\_database.sql

│   

│   └── queries.sql

│

├── charts/

│   ├── production\_status.png

│   ├── monthly\_orders.png

│   ├── supplier\_spend.png

│   ├── forecast\_vs\_actual.png

│   ├── work\_center\_load.png

│   ├── order\_priority.png

│   └── invoice\_validation.png

│

└── README.md

🔄 Project Workflow

1\. Data Generation (Python)

Generated 500+ synthetic records using Faker

Created four datasets:

Manufacturing Orders

Purchase Orders

Sales Orders

Vendor Invoices

2\. Data Cleaning \& Validation

Removed duplicates

Handled missing values

Standardized date formats (YYYY-MM-DD)

Recalculated:

Pending Quantity

Forecast Error

Applied invoice validation rules

3\. SQL Database Layer

Created relational tables in MySQL

Loaded cleaned CSV files

Built joins between:

Manufacturing ↔ Purchase Orders

Purchase Orders ↔ Vendor Invoices

📊 Key KPIs

📉 Delay Percentage

⚙️ Production Efficiency

🚚 Supplier Performance (Fulfillment Rate)

💰 Invoice Mismatch Rate

📦 Work Center Load

📈 Forecast vs Actual Production

🧾 Sales Revenue by Customer

📌 SQL Insights Examples

\-- Production Efficiency

SELECT

&#x20;   ROUND(SUM(Completed\_Qty)/SUM(Quantity)\*100,2) AS Efficiency

FROM Manufacturing\_Orders;

\-- Invoice Mismatch Rate

SELECT

&#x20;   ROUND(

&#x20;       SUM(CASE WHEN Validation\_Status='Mismatch' THEN 1 ELSE 0 END)

&#x20;       / COUNT(\*) \* 100,2

&#x20;   ) AS Mismatch\_Rate

FROM Vendor\_Invoices;

📊 Python Visualizations



Generated charts:



Production Status Distribution (Pie Chart)

Monthly Manufacturing Orders (Line Chart)

Supplier Spend Analysis (Bar Chart)

Forecast vs Actual Production

Work Center Load Analysis

Order Priority Distribution

Invoice Validation Status



💡 Business Insights

Identified production delays by work center

Analyzed supplier performance based on delivery fulfillment

Detected invoice mismatches before finance approval

Compared forecast vs actual production accuracy

Tracked high-priority manufacturing bottlenecks

Improved visibility into end-to-end supply chain workflow

🎯 Key Learnings

End-to-end ETL pipeline design

ERP-style data modeling

SQL-based KPI analysis

Python data visualization

Business intelligence storytelling

Manufacturing operations analytics



👤 Author



Madhu Bharti

Aspiring Data Analyst

Skills: Python | SQL | Power BI | Excel | Data Analytics

