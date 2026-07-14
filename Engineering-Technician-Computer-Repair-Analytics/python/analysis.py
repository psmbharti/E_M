import pandas as pd

# Load dataset
df = pd.read_csv(r"data/computer_repairs_clean.csv")

# -----------------------------
# 1. Total repairs completed
# -----------------------------
total_repairs = len(df)

# -----------------------------
# 2. Failure rate
# -----------------------------
failure_rate = df['Failure_Category'].value_counts(normalize=True) * 100

# -----------------------------
# 3. Average repair time
# -----------------------------
avg_repair_time = df[round('Repair_Time_Hours' , 2)].mean()

# -----------------------------
# 4. Most common repair categories
# -----------------------------
common_categories = df['Failure_Category'].value_counts()

# -----------------------------
# 5. Technician productivity
# -----------------------------
technician_productivity = df.groupby('Engineer').agg(
    Repairs_Completed=('Repair_ID', 'count'),
    Avg_Repair_Time=('Repair_Time_Hours', 'mean'),
    Avg_Satisfaction=('Customer_Satisfaction', 'mean')
).sort_values('Repairs_Completed', ascending=False)

# -----------------------------
# 6. Pass vs Fail counts
# -----------------------------
qc_pass_fail = df['QC_Status'].value_counts()

# -----------------------------
# 7. MTTR (Mean Time to Repair)
# -----------------------------
mttr = df['Repair_Time_Hours'].mean()

# -----------------------------
# 8. Median repair time
# -----------------------------
median_repair_time = df['Repair_Time_Hours'].median()

# -----------------------------
# 9. Cost per category
# -----------------------------
cost_per_category = df.groupby('Failure_Category')['Repair_Cost'].mean()

# -----------------------------
# 10. Rework rate
# -----------------------------
rework_rate = df['Rework'].value_counts(normalize=True) * 100

# -----------------------------
# 11. QC pass/fail distribution
# -----------------------------
qc_distribution = df['QC_Status'].value_counts(normalize=True) * 100

# -----------------------------
# 12. Satisfaction score analysis
# -----------------------------
satisfaction_summary = df['Customer_Satisfaction'].describe()

# -----------------------------
# 13. Warehouse performance
# -----------------------------
warehouse_performance = df.groupby('Warehouse').agg(
    Repairs=('Repair_ID', 'count'),
    Avg_Time=('Repair_Time_Hours', 'mean'),
    Avg_Cost=('Repair_Cost', 'mean')
)

# -----------------------------
# 14. Supplier reliability metrics
# -----------------------------
supplier_metrics = df.groupby('Supplier').agg(
    Repairs=('Repair_ID', 'count'),
    Avg_Satisfaction=('Customer_Satisfaction', 'mean'),
    Avg_Cost=('Repair_Cost', 'mean')
).sort_values('Avg_Satisfaction', ascending=False)

# -----------------------------
# Print summary
# -----------------------------
print("\n===== Repair Analytics Summary =====\n")
print(f"Total Repairs Completed: {total_repairs}")
print("\nFailure Rate (%):\n", failure_rate)
print("\nAverage Repair Time (hrs):", avg_repair_time)
print("\nMedian Repair Time (hrs):", median_repair_time)
print("\nMost Common Repair Categories:\n", common_categories)
print("\nTechnician Productivity:\n", technician_productivity)
print("\nQC Pass vs Fail Counts:\n", qc_pass_fail)
print("\nCost per Category:\n", cost_per_category)
print("\nRework Rate (%):\n", rework_rate)
print("\nQC Distribution (%):\n", qc_distribution)
print("\nSatisfaction Score Summary:\n", satisfaction_summary)
print("\nWarehouse Performance:\n", warehouse_performance)
print("\nSupplier Reliability Metrics:\n", supplier_metrics)
print("\n====================================\n")
