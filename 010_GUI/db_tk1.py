from tkinter import *
from tkinter import messagebox
import mysql.connector as sql

# DB Connection
con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="19feb_python"
)
cursor = con.cursor()

# Main Window
root = Tk()
root.geometry("500x500")
root.title("Student Form")
root.config(bg="#2c3e50")  # Dark background

# Frame (Card style)
frame = Frame(root, bg="white", bd=0)
frame.place(x=50, y=50, width=400, height=400)

# Title
title = Label(frame, text="Student Registration",
              font=("Arial", 16, "bold"),
              bg="white", fg="#2c3e50")
title.pack(pady=20)

# Function
def create():
    name = t1.get()
    email = t2.get()
    phone = t3.get()

    if name == "" or email == "" or phone == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    qry = "insert into student values(%s,%s,%s,%s)"
    val = (0, name, email, phone)
    cursor.execute(qry, val)
    con.commit()

    messagebox.showinfo("Success", "Data Inserted Successfully!")

    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)

# Label + Entry Style
def styled_entry(parent):
    e = Entry(parent, font=("Arial", 12), bd=1, relief=SOLID)
    return e

# Username
Label(frame, text="Username", font=("Arial", 11),
      bg="white").pack(anchor="w", padx=40)
t1 = styled_entry(frame)
t1.pack(padx=40, pady=5, fill="x")

# Email
Label(frame, text="Email", font=("Arial", 11),
      bg="white").pack(anchor="w", padx=40)
t2 = styled_entry(frame)
t2.pack(padx=40, pady=5, fill="x")

# Phone
Label(frame, text="Phone", font=("Arial", 11),
      bg="white").pack(anchor="w", padx=40)
t3 = styled_entry(frame)
t3.pack(padx=40, pady=5, fill="x")

# Button hover effect
def on_enter(e):
    btn.config(bg="#1abc9c")

def on_leave(e):
    btn.config(bg="#16a085")

# Submit Button
btn = Button(frame, text="Submit",
             font=("Arial", 12, "bold"),
             bg="#16a085", fg="white",
             bd=0, padx=10, pady=8,
             cursor="hand2",
             command=create)
btn.pack(pady=30)

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

root.mainloop()