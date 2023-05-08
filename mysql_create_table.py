import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="password", database="client_db")
cur = conn.cursor()

cmd = "CREATE TABLE clients (\
    ClientID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    ClientName VARCHAR(50) NOT NULL,\
    ClientPhone VARCHAR(30), \
    ClientWatch VARCHAR(75), \
    TotalSpent VARCHAR(15))"

cur.execute(cmd)
conn.close()