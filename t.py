import pandas as pd
df = pd.read_csv('data2025.csv')
print(df['Date'].min(), df['Date'].max())
print(df['RegionName'].nunique())
print(df['RegionName'].unique()[:20])