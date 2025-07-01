import mysql.connector

mydb = mysql.connector.connect(
    
    host = "localhost",
    port = "3306",
    user = "root",
    password = "Manasa@123"
)


#print("mydb") 

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

#mycursor = mydb.cursor()

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
  #print(x)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#mycursor = mydb.cursor()

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
     #print(x)






