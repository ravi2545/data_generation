import numpy as np
import pandas as pd

# Generate random data
num_rows = 30**6  # 1 million rows
data = {
    'column1': np.random.randint(0, 100, size=num_rows),
    'column2': np.random.rand(num_rows),
    'column3': np.random.choice(['A', 'B', 'C', 'D'], size=num_rows)
}
df = pd.DataFrame(data)
df = pd.DataFrame(data)
# Write DataFrame to CSV
df.to_csv('large_data_30.csv', index=False)