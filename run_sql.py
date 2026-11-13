"""Run a .sql file against olist.db and print the result.   Usage: python run_sql.py queries/01_order_status.sql"""
import sqlite3
import sys

import pandas as pd

sql = open(sys.argv[1], encoding="utf-8").read()
conn = sqlite3.connect("olist.db")
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
print(pd.read_sql_query(sql, conn).to_string(index=False))
conn.close()