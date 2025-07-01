import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Manasa@123",
    database = "mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE electricitems (name VARCHAR(255), color VARCHAR(255), kg VARCHAR(220) )")

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
  #print(x)

#sql = "insert into electricitems (name,color,kg) values (%s,%s,%s)"
#val = ("hairdryer", "black","1kg")
#mycursor.execute(sql,val)
#mydb.commit
#print(mycursor.rowcount,"record insert")       

#sql ="insert into electricitems (name,color,kg) values (%s,%s,%s)"
#val = [
  #("iphone","white","1kg"),
 # ("laptop","pink","2kg")
#]
#mycursor.executemany(sql,val)
#mydb.commit
#print(mycursor.rowcount,"records insert")

#mycursor.execute("SELECT * FROM electriccitems")
#myresult = mycursor.fetchall()
#for x in myresult:
 # print(x)


#sql = "DELETE FROM electricitems WHERE name='iphone'"
#mycursor.execute(sql)
#mydb.commit
#print(mycursor.rowcount,"delete records")

sql ="UPDATE electricitems SET name = 'laptop' WHERE  name = 'valley234'"
mycursor.execute(sql)
mydb.commit
print(mycursor.rowcount, "update records")




