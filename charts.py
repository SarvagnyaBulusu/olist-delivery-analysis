import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)
conn = sqlite3.connect("olist.db")

def run(path):
    with open(path, encoding="utf-8") as f:
        return pd.read_sql(f.read(), conn)

# Chart 1: review score by how late the order was
d = run("queries/05_reviews_by_days_late.sql")
labels = d["delay_bucket"].str[3:]
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(labels, d["avg_review_score"],
              color=["#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"])
ax.bar_label(bars, fmt="%.2f")
ax.set_ylim(0, 5)
ax.set_ylabel("Average review score (1-5)")
ax.set_title("Reviews collapse once an order is more than 3 days late")
plt.tight_layout()
plt.savefig("charts/reviews_by_delay.png", dpi=150)
plt.close()

# Chart 2: late-delivery rate by state
s = run("queries/04_late_by_state.sql").sort_values("late_pct")
fig, ax = plt.subplots(figsize=(8, 7))
ax.barh(s["customer_state"], s["late_pct"], color="#e76f51")
ax.axvline(8.1, color="black", linestyle="--")
ax.text(8.4, 0.2, "Overall: 8.1%")
ax.set_xlabel("Late deliveries (% of delivered orders)")
ax.set_title("Northeast states have the highest late-delivery rates")
plt.tight_layout()
plt.savefig("charts/late_by_state.png", dpi=150)
plt.close()

print("Saved 2 charts in the charts folder")