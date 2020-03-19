import mysql.connector
mydb = mysql.connector.connect(
  host="192.168.1.237",
  port="3307",
  user="root",
  passwd="zgadmin",
  database='datav'
)
# print(mydb)
mycursor = mydb.cursor()
mycursor.execute("select * from t_test")
myresult = mycursor.fetchall()
one = mycursor.fetchone()
print(one)
for x in myresult:
	print(x)
