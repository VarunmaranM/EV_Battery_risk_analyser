import pandas as pd
import numpy as np

# Number of data points
num_rows = 200

# Generate realistic data
data = {
    'temperature': np.random.normal(35, 10, num_rows),
    'voltage': np.random.normal(3.9, 0.15, num_rows),
    'current': np.random.normal(15, 5, num_rows),
    'charge_cycles': np.random.randint(50, 800, num_rows),
    'health_score': np.random.randint(70, 101, num_rows)
}

df = pd.DataFrame(data)

# Define risk level based on rules
def assign_risk(row):
    if row['health_score'] < 80 or row['temperature'] > 55 or row['temperature'] < 5:
        return 'High'
    elif 80 <= row['health_score'] < 90 or 45 < row['temperature'] <= 55:
        return 'Medium'
    else:
        return 'Low'

df['risk_level'] = df.apply(assign_risk, axis=1)

# Save to CSV
df.to_csv('battery_data.csv', index=False)

print("battery_data.csv generated successfully with 200 rows.")