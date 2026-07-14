import pandas as pd

df = pd.read_csv(r"data/computer_repairs_clean.csv")

summary = df.groupby("Failure_Category").agg(
    Total_Repairs=("Repair_ID", "count"),
    Average_Time=("Repair_Time_Hours", "mean")
)

summary.to_excel(r"reports/Repair_Summary.xlsx", index=True)
print("Report created successfully.")


