import mysql.connector

# connecting to db
con=mysql.connector.connect(host="localhost",port="3306",user="root",passwd="Tashu@6202",database="gits47")
if con:
    print("DB Connected")
else:
    print("DB not Connected")

# creating cursor to carry sql
cursor=con.cursor()
no=input("Enter Account Number:")
name=input("Enter AC name:")
bal=input("Enter AC Balance:")
dt=input("Enter Account Actvation Date:")
city=input("Enter City:")
sql="insert into accountmaster values("+no+",'"+name+"',"+bal+",'"+dt+"','"+city+"');"
cursor.execute(sql)
#commiting SQL
con.commit()
if cursor.rowcount>0:
    print("Data Inserted")
else:
    print("Data not Inserted")    
# retrieving data
sql="select * from accountmaster;"
cursor.execute(sql)
# fetching all records
result=cursor.fetchall()
for item in result:
    print(item)
# closing connection
cursor.close()
con.close()

                