import pandas as pd
import numpy as np
import random

np.random.seed(42)

n = 10000
data = []

for i in range(1, n + 1):

    customer_type = random.choice(["loyal", "neutral", "at_risk"])

    if customer_type == "loyal":
        monthly_spend = np.random.randint(250, 500)
        login_frequency = np.random.randint(18, 30)
        support_tickets = np.random.randint(0, 2)
        days_inactive = np.random.randint(0, 12)

    elif customer_type == "neutral":
        monthly_spend = np.random.randint(120, 300)
        login_frequency = np.random.randint(8, 20)
        support_tickets = np.random.randint(1, 4)
        days_inactive = np.random.randint(8, 25)

    else:
        monthly_spend = np.random.randint(20, 180)
        login_frequency = np.random.randint(1, 10)
        support_tickets = np.random.randint(3, 8)
        days_inactive = np.random.randint(20, 60)

    subscription_type = random.choice(["Basic", "Standard", "Premium"])
    region = random.choice(["North", "South", "East", "West"])

    risk_score = 0

    if days_inactive > 35:
        risk_score += 3
    elif days_inactive > 20:
        risk_score += 2

    if support_tickets > 5:
        risk_score += 2
    elif support_tickets > 2:
        risk_score += 1

    if login_frequency < 8:
        risk_score += 2

    if monthly_spend < 150:
        risk_score += 1

    if subscription_type == "Basic":
        risk_score += 1
    elif subscription_type == "Premium":
        risk_score -= 1

    probability_map = {
        -1: 0.03,
        0: 0.08,
        1: 0.18,
        2: 0.35,
        3: 0.60,
        4: 0.82,
        5: 0.93,
        6: 0.97,
        7: 0.99
    }

    risk = probability_map.get(risk_score, 0.97)

    is_churned = np.random.choice([0, 1], p=[1 - risk, risk])

    data.append([
        i,
        monthly_spend,
        login_frequency,
        support_tickets,
        days_inactive,
        subscription_type,
        region,
        is_churned
    ])

df = pd.DataFrame(data, columns=[
    "customer_id",
    "monthly_spend",
    "login_frequency",
    "support_tickets",
    "days_inactive",
    "subscription_type",
    "region",
    "is_churned"
])

df.to_csv("customers.csv", index=False)

print("Done")