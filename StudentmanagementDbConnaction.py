import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Manasa@123",
    database = "mydatabase"
)

mycursor = mydb.cursor

#mycursor.execute("create database mydatabase")
#print("create successfully")

mycursor.execute("show tables")
for x in mycursor:
    print(x)
