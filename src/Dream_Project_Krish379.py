# Dream Project Script

import pandas as pd

# Update the path references to point to the ../data/ directory
csv_file_path = '../data/sample_data.csv'

# Sample operation
try:
    data = pd.read_csv(csv_file_path)
    print(data.head())
except FileNotFoundError:
    print(f'File not found: {csv_file_path}')