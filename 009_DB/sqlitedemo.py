import sqlite3

con = sqlite3.connect("data.db")

# qry = "create table student(id int,name varchar(20),email varchar(20))"

# qry = "insert into student values(3,'Priyanshu','sufi@gmail.com')"

# qry = "update student set name='sf' where id=2 "

# qry = "delete from student where id=1"

# con.execute(qry)
# con.commit()


data = con.execute("select * from student").fetchall()
print(data)
