import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv("customers.csv")

# Create SQLite database
conn = sqlite3.connect("customer_churn.db")

# Load data into SQL table
df.to_sql("customers", conn, if_exists="replace", index=False)

print("Database created successfully")

conn.close()