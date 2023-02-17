import mysql.connector as con
mydb=con.connect(
    host="localhost",
    username="abc",
    password="password",
    database="Test_db"
)

cursor=mydb.cursor()
query="insert into Employee_TBL(EmployeeName,Age,Weight,Address) values('{}',{},{},'{}')".format("mari",23,65,"salem")
print("query",query)
#cursor.execute(query)
cursor.execute("select *from Employee_TBL")
print("cursor",cursor)
# mydb.commit()
for data in cursor:
    print("data",data)
cursor.close()