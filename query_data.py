import sqlite3
import pandas as pd


# Connect to the existing database
conn = sqlite3.connect("movies.db")

df=pd.read_sql_query("select *from movies where genre='Comedy';", conn)
#df=pd.read_sql_query('Select *from movies ORDER BY year asc',conn)
#df=pd.read_sql_query("select name,SUBSTR(year,1,4) as release_year, revenue_millions from movies where genre='Action' ORDER BY release_year asc, revenue_millions DESC Limit 15;", conn)
df['release_year'] = pd.to_datetime(df['year']).dt.year  # Extract year only
df = df.sort_values(by=['release_year', 'revenue_millions'], ascending=[True, False])
df = df.head(5)

# Replace 0s with fixed default values
df['rating'] = df['rating'].replace(0, 5)
df['metascore'] = df['metascore'].replace(0, 50)

conn.close()
print(df)


'''
# Calculate medians (excluding 0s)
rating_median=df[df['rating'] !=0]['rating'].median()
metascore_median=df[df['metascore']!=0]['metascore'].median()

rating_median = df[df['rating'] != 0]['rating'].median()
if pd.isna(rating_median):
    rating_median = 5  # Default fallback value

metascore_median = df[df['metascore'] != 0]['metascore'].median()
if pd.isna(metascore_median):
    metascore_median = 50  # Default fallback value
# Replace 0s with median
df['rating'] = df['rating'].replace(0, rating_median)
df['metascore'] = df['metascore'].replace(0, metascore_median)


print(df['rating'].unique())
print(df['metascore'].unique())
'''