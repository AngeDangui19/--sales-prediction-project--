import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("sales.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS sales")

cur.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER,
    date TEXT
)
""")

products = [
    ("Stylo", "Office"),
    ("Cahier", "Office"),
    ("Clé USB", "Tech"),
    ("Clavier", "Tech"),
    ("Casque", "Tech"),
    ("Sac", "Accessoires")
]

start_date = datetime(2024, 1, 1)

for i in range(400):
    p, c = random.choice(products)
    price = round(random.uniform(5, 100), 2)
    quantity = random.randint(1, 5)
    date = start_date + timedelta(days=random.randint(0, 450))

    cur.execute(
        "INSERT INTO sales (product, category, price, quantity, date) VALUES (?, ?, ?, ?, ?)",
        (p, c, price, quantity, date.strftime("%Y-%m-%d"))
    )

conn.commit()
conn.close()

print("Database created")
