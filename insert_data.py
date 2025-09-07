import sqlite3
import pandas as pd
import numpy as np

# Load the CSV
df = pd.read_csv(r"C:\Users\Akash\Downloads\Movie-Data.csv")
df.columns = df.columns.str.strip()

# Select only the required columns
df = df[['Movie Title', 'Genre', 'Release Date', 'Revenue']]

# Rename to match DB schema
df.rename(columns={
    'Movie Title': 'name',
    'Genre': 'genre',
    'Release Date': 'year',
    'Revenue': 'revenue_millions'
}, inplace=True)

# Clean revenue column
df['revenue_millions'] = (
    df['revenue_millions']
    .astype(str)
    .str.replace(r'[\$,]', '', regex=True)
    .replace('None', np.nan)
    .astype(float)
)

# 👉 Convert dollars to millions
df['revenue_millions'] = df['revenue_millions'] / 1_000_000


# Fill missing revenue with median
df['revenue_millions'] = df['revenue_millions'].fillna(df['revenue_millions'].median())

# Add dummy rating + metascore
df['rating'] = 0
df['metascore'] = 0

# Drop rows with missing essential info
df.dropna(subset=['name', 'genre', 'year'], inplace=True)

# Reorder columns to match SQL
df = df[['name', 'rating', 'genre', 'year', 'revenue_millions', 'metascore']]

# Save to SQLite
conn = sqlite3.connect("movies.db")
df.to_sql("movies", conn, if_exists="replace", index=False)
conn.close()

print("✅ Final cleaned data inserted successfully.")
print(df.isnull().sum())
