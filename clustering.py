import sqlite3
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

conn = sqlite3.connect("sales.db")
df = pd.read_sql("SELECT * FROM sales", conn)
conn.close()

df["revenue"] = df["price"] * df["quantity"]

product_df = df.groupby("product").agg({
    "revenue": "sum",
    "price": "mean",
    "quantity": "sum"
})

scaler = StandardScaler()
X = scaler.fit_transform(product_df)

kmeans = KMeans(n_clusters=3, random_state=0)
product_df["cluster"] = kmeans.fit_predict(X)

print(product_df)
