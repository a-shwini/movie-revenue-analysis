import sqlite3
print("✅ SQLite is working")

# Connect or create DB
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# Drop if exists (for testing purposes)
cursor.execute("DROP TABLE IF EXISTS movies")

# Create a table based on your CSV columns
cursor.execute("""
    CREATE TABLE movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rating REAL,
        genre TEXT,
        year INTEGER,
        revenue_millions REAL,
        metascore INTEGER
    )
""")

conn.commit()
conn.close()

print("✅ Table created successfully.")

'''
import pandas
import numpy
import matplotlib
import seaborn

print("✅ All libraries are working!")
exit()
'''