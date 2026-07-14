# 🔧 Computer Repairs Analytics & Engineering Reports  
A complete end‑to‑end analytics system for computer repair operations, including data ingestion, SQL modeling, engineering KPIs, quality metrics, process improvement insights, and automated PDF report generation with charts.

---

## 📁 Project Structure
project/
│
├── data/
│   └── computer_repairs_clean.csv
│
├── reports/
│   ├── Quality_Test_Report.pdf
│   ├── Engineering_Report.pdf
│   └── Process_Improvement_Report.pdf
│
├── sql/
│   ├── create_tables.sql
│   ├── load_data.sql
│   ├── analysis_queries.sql
│   └── views.sql
│
├── scripts/
│   ├── generate_quality_test_report.py
│   ├── generate_engineering_report.py
│   └── generate_process_improvement_report.py
│
└── README.md


---

## 📊 Project Overview

This project analyzes **500+ computer repair records** and generates:

### ✔ Quality Metrics  
- QC pass vs fail  
- Rework rate  
- Satisfaction distribution  
- Failure category frequency  

### ✔ Engineering Metrics  
- Technician productivity  
- Device type performance  
- Failure type analysis  

### ✔ Process Improvement Metrics  
- MTTR (Mean Time to Repair)  
- Median repair time  
- Cost per category  
- Warehouse efficiency  
- Supplier reliability  

Each report includes:

- **Tables with dark‑blue corporate headers (#003366)**  
- **Charts (bar, pie, histogram)**  
- **Clean PDF formatting**  

---

## 🗂 SQL Layer

The SQL folder contains:

### **1. create_tables.sql**  
Defines the full relational schema for:

- Computer_Repairs  
- Employees  
- Suppliers  
- Warehouses  
- Parts  

### **2. load_data.sql**  
Loads the CSV into MySQL using `LOAD DATA INFILE`.

### **3. views.sql**  
Reusable engineering views:

- Quality_Performance  
- Technician_Performance  
- Failure_Analysis  
- Warehouse_Efficiency  
- Supplier_Reliability  

### **4. analysis_queries.sql**  
All operational KPIs including:

- Total repairs  
- QC metrics  
- MTTR  
- Median repair time (MySQL‑compatible)  
- Cost analysis  
- Warehouse & supplier performance  

---

## 🐍 Python Layer

Three Python scripts generate the PDF reports:

### **generate_quality_test_report.py**
Includes:

- QC tables  
- Rework tables  
- Satisfaction tables  
- Failure category tables  
- Charts embedded in PDF  

### **generate_engineering_report.py**
Includes:

- Technician productivity  
- Device performance  
- Failure type analysis  
- Charts embedded in PDF  

### **generate_process_improvement_report.py**
Includes:

- MTTR & median time  
- Cost per category  
- Warehouse performance  
- Supplier reliability  
- Charts embedded in PDF  

All reports use:

- **ReportLab** for PDF  
- **Matplotlib** for charts  
- **Dark blue header styling (#003366)**  

---

## 📈 Sample KPIs

| Metric | Description |
|--------|-------------|
| MTTR | Mean Time to Repair |
| Median Repair Time | 50th percentile repair duration |
| QC Pass Rate | % of repairs passing quality check |
| Rework Rate | % of repairs requiring rework |
| Technician Productivity | Repairs per engineer |
| Supplier Reliability | Avg satisfaction per supplier |
| Warehouse Efficiency | Repairs + avg time + avg cost |

---


