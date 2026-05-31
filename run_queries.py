import sqlite3
import pandas as pd
import time

conn = sqlite3.connect("customer_churn.db")

queries = {

    "Customer Segmentation": """
    SELECT
        customer_id,
        monthly_spend,
        CASE
            WHEN monthly_spend >= 300 THEN 'High Value'
            WHEN monthly_spend >= 150 THEN 'Medium Value'
            ELSE 'Low Value'
        END AS customer_segment
    FROM customers
    LIMIT 20;
    """,

    "Churn Rate by Subscription": """
    SELECT
        subscription_type,
        ROUND(AVG(is_churned) * 100, 2) AS churn_rate
    FROM customers
    GROUP BY subscription_type;
    """,

    "Top Revenue Customers": """
    SELECT
        customer_id,
        monthly_spend,
        RANK() OVER (ORDER BY monthly_spend DESC) AS revenue_rank
    FROM customers
    LIMIT 10;
    """,

    "Retention Trend": """
    SELECT
        region,
        COUNT(*) AS active_customers
    FROM customers
    WHERE is_churned = 0
    GROUP BY region;
    """
}

for title, query in queries.items():
    start = time.time()

    result = pd.read_sql(query, conn)

    end = time.time()

    print(f"\n===== {title} =====")
    print(result)
    print(f"\nExecution Time: {end - start:.5f} seconds")

conn.close()