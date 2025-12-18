import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")
df = pd.read_sql("SELECT * FROM sales", conn)
conn.close()

df["date"] = pd.to_datetime(df["date"])
df["revenue"] = df["price"] * df["quantity"]
df["month"] = df["date"].dt.to_period("M")

print(df.head())

print("\nRevenue by product")
print(df.groupby("product")["revenue"].sum())

print("\nRevenue by category")
print(df.groupby("category")["revenue"].sum())

print("\nMonthly revenue")
print(df.groupby("month")["revenue"].sum())
