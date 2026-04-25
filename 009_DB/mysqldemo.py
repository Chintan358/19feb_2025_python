import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user = "root",
    password="root",
    database="19feb_python"
)

cursor = con.cursor()

# cursor.execute("create database 19feb_python")

# cursor.execute("create table student(id int primary key,name varchar(20), email varchar(50))")

cursor.execute("insert into student values(1,'mohit','mohit@gmail.com')")
con.commit()