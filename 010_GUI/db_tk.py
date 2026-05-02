from tkinter import *
import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="19feb_python"
)

cursor = con.cursor()



root = Tk()
root.geometry("500x500")
root.title("MyAPP")

def create():
    name = t1.get()
    email = t2.get()
    phone = t3.get()
    # cursor.execute(f"insert into student values({name},{email},{phone})")
    qry = "insert into student values(%s,%s,%s,%s)"
    val = (0,name,email,phone)
    cursor.execute(qry,val)
    con.commit()
    
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)

l1 = Label(root,text="Username").place(x=100,y=100)
l2 = Label(root,text="Email").place(x=100,y=150)
l3 = Label(root,text="Phone").place(x=100,y=200)


t1 = Entry(root)
t1.place(x=200,y=100)
t2 = Entry(root)
t2.place(x=200,y=150)
t3 = Entry(root)
t3.place(x=200,y=200)

b1 = Button(root,text="submit",width=15, command=create).place(x=200,y=250)

root.mainloop()