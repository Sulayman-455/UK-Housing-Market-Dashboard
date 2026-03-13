import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv('data2025.csv')

# Filter 2010 onwards only
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df = df[df['Date'] >= '2010-01-01']

# Clean column names - remove special characters
df.columns = df.columns.str.replace('%', 'Pct').str.replace(' ', '_')

# Load into SQLite database
engine = create_engine('sqlite:///housing.db')
df.to_sql('housing_data', engine, if_exists='replace', index=False)

print(f"Done. {len(df)} rows loaded into housing.db")
