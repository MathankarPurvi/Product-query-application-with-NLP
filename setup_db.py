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
    ("Coffee Maker", "Appliances", 80.00, "White"),
     ("Refrigerator", "Appliances", 899.99, "White"),
    ("Microwave", "Appliances", 199.99, "Black"),
    ("Sneakers", "Footwear", 75.00, "White"),
    ("Backpack", "Accessories", 45.00, "Blue"),
    ("Smartwatch", "Electronics", 249.99, "Black"),
    ("Tablet", "Electronics", 399.99, "Gray"),
    ("Dress", "Clothing", 60.00, "Red"),
    ("Desk Lamp", "Furniture", 30.00, "Yellow"),
    ("Office Chair", "Furniture", 150.00, "Black"),
    ("Running Shoes", "Footwear", 90.00, "Green"),
    ("Blender", "Appliances", 70.00, "Silver"),
    ("Gaming Console", "Electronics", 499.99, "Black"),
    ("Bicycle", "Sports", 250.00, "Red"),
    ("Helmet", "Sports", 50.00, "White"),
    ("Jacket", "Clothing", 120.00, "Brown"),
    ("Electric Kettle", "Appliances", 40.00, "Black"),
    ("Sunglasses", "Accessories", 25.00, "Black"),
    ("Cookware Set", "Kitchenware", 300.00, "Gray"),
    ("Bookshelf", "Furniture", 200.00, "Brown"),
    ("Dining Table", "Furniture", 800.00, "Oak"),
    ("Yoga Mat", "Sports", 30.00, "Purple"),
    ("Water Bottle", "Accessories", 15.00, "Green"),
    ("Camera", "Electronics", 800.00, "Black"),
    ("Tripod", "Electronics", 50.00, "Silver"),
    ("Air Purifier", "Appliances", 250.00, "White"),
    ("Winter Coat", "Clothing", 200.00, "Navy Blue"),
    ("Basketball", "Sports", 25.00, "Orange"),
    ("Perfume", "Accessories", 60.00, "Transparent"),
    ("Wall Clock", "Home Decor", 45.00, "Gold")
]
cursor.executemany("INSERT INTO products (name, category, price, color) VALUES (?, ?, ?, ?)", products)

conn.commit()
conn.close()
print("Database setup complete!")
