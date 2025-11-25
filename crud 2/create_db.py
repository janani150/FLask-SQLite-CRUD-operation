import sqlite3 as sql

# Connect to SQLite
con = sql.connect('db_web.db')

# Create a cursor
cur = con.cursor()

# Drop users table if it already exists
cur.execute("DROP TABLE IF EXISTS users")

# Create users table with new structure
sql_create = '''CREATE TABLE "users" (
    "UID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT,
    "number" TEXT,
    "address" TEXT,
    "email" TEXT,
    "age" INTEGER
)'''
cur.execute(sql_create)

# Commit changes
con.commit()

# Close the connection
con.close()
