import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Manasa@123",
    database = "mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("create database mydatabase")
print("Database checked or created successfully.")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
  #print(x)

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), schoolname VARCHAR(255))")
#print("Table 'customers' checked or created successfully.")

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
     #print(x)

#sql = "INSERT INTO customers (name, schoolname) VALUES (%s, %s)"
#val = [
  #  ("John", "z.p.h.school"),
 #   ("manasa","wisdom school")
#]
    
#mycursor.executemany(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record was  inserted.")...............  # insert query  


#.........select query...................

#mycursor.execute("SELECT * FROM customers")

#myresult = mycursor.fetchall()

#for x in myresult:
  #print(x)

#mycursor.execute("SELECT name, schoolname FROM customers")

#myresult = mycursor.fetchall()

#for x in myresult:
  #print(x)  

#mycursor.execute("SELECT * FROM customers")

#myresult = mycursor.fetchone()

#print(myresult)  ......................................select query.........................

#sql = "DELETE FROM customers WHERE schoolname= 'z.p.h.school'"

#mycursor.execute(sql)

#mydb.commit()

#print(mycursor.rowcount, "record(s) deleted")  ................delete query................

#sql = "UPDATE customers SET schoolname = 'golden valley' WHERE schoolname = 'wisdom'"

#mycursor.execute(sql)

#mydb.commit()

#print(mycursor.rowcount, "record(s) affected")     .....................update query.........








