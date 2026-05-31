import sqlite3
import time

conn = sqlite3.connect("customer_churn.db")
cursor = conn.cursor()

query = """
SELECT *
FROM customers
WHERE subscription_type = 'Basic'
AND days_inactive > 30
"""

# Before index
start = time.time()
cursor.execute(query).fetchall()
before = time.time() - start

# Create index
cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_churn
ON customers(subscription_type, days_inactive)
""")

conn.commit()

# After index
start = time.time()
cursor.execute(query).fetchall()
after = time.time() - start

print(f"Before Index: {before:.6f} sec")
print(f"After Index: {after:.6f} sec")

conn.close()