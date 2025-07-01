import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Manasa@123",
    database = "mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE A TABLE person(name VARCHAR(332),(color VARCHAR(234), height VARCHAR(567)))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

#sql = "INSERT INTO person (name,color) VALUES(%s,%s)"
#val = ("manasa","white")

#mycursor.execute(sql,val)
#mydb.commit()
#sprint(mycursor.rowcount,"insert records")

#sql ="INTER INTO person (name ,color) VALUES (%s,%s)"
#val = [
  #  ("manas","red"),
 #   ("anbu","black")
#]
#mycursor.execute(sql,val)
#mydb.commit()
#print(mycursor.execute,"insert many records")

#mycursor.execute("SELECT * FRROM person")
#myresult = mycursor.fetchall()
#for x in myresult:
 #   print(x)

#mycursor.execute("SELECT * name,color from person")
#myresult = mycursor.fetchall()
#for x in myresult:
 #   print(x)


#sql = "DELECT FROM person WHERE color ='red'"
#mycursor.execute(sql)
#mydb.commit()
#print(mycursor.execute,"delete records")


#sql = "UPDATE person SET color = green WHERE color = VALUES(234)"
#mycursor.execute(sql)
#mydb.commit()
#print(mycursor.execute,"update records")
