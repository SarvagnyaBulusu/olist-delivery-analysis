import os
import sqlite3
import pandas as pd

os.makedirs("powerbi", exist_ok=True)
conn = sqlite3.connect("olist.db")

for name in ["04_late_by_state", "05_reviews_by_days_late"]:
    with open(f"queries/{name}.sql", encoding="utf-8") as f:
        pd.read_sql(f.read(), conn).to_csv(f"powerbi/{name}.csv", index=False)

print("Exported CSVs to the powerbi folder")