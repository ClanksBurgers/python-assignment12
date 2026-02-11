
import os
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect(os.path.join('..', 'db', 'lesson.db'))

# SQL to get order_id and total_price for each order
query = '''
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
'''
df = pd.read_sql_query(query, conn)
conn.close()

# Calculate cumulative revenue
# Option 1: Using apply (as described)
def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()
# Uncomment below to use apply method
# df['cumulative'] = df.apply(cumulative, axis=1)

# Option 2: Using cumsum (recommended)
df['cumulative'] = df['total_price'].cumsum()

# Plot cumulative revenue vs. order_id
plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o', color='green')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')
plt.title('Cumulative Revenue by Order')
plt.grid(True)
plt.tight_layout()
plt.show()
