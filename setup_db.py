import sqlite3


conn = sqlite3.connect("tmp/data.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price REAL,
        color TEXT
    )
""")

products = [
    ("Smartphone", "Electronics", 699.99, "Black"),
    ("Laptop", "Electronics", 1200.00, "Silver"),
    ("T-Shirt", "Clothing", 20.00, "Blue"),
    ("Headphones", "Electronics", 150.00, "Red"),
    ("Coffee Maker", "Appliances", 80.00, "White")
]
cursor.executemany("INSERT INTO products (name, category, price, color) VALUES (?, ?, ?, ?)", products)

conn.commit()
conn.close()
print("Database setup complete!")
