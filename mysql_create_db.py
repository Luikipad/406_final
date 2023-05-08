import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="password")
cur = conn.cursor()

# Test connection
print(conn)

cmd = "CREATE DATABASE client_db"
cur.execute(cmd)
conn.close()