"""Load the Olist CSV files into a SQLite database (olist.db) so we can query them with SQL."""
import sqlite3
from pathlib import Path

import pandas as pd

DATA_DIR = Path("data")
DB_FILE = Path("olist.db")

conn = sqlite3.connect(DB_FILE)

for csv_file in sorted(DATA_DIR.glob("*.csv")):
    # olist_orders_dataset.csv  ->  table "orders"
    table = csv_file.stem.replace("olist_", "").replace("_dataset", "")
    df = pd.read_csv(csv_file)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"{table:35} {len(df):>9,} rows   {len(df.columns):>2} columns")

conn.close()
print(f"\nDone. Database saved as {DB_FILE}")