from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("MyAPP")

# b1 = Button(root,text="left").pack(side=LEFT)
# b2 = Button(root,text="right").pack(side=RIGHT)
# b3 = Button(root,text="top").pack(side=TOP)
# b4 = Button(root,text="bottom").pack(side=BOTTOM)

# l1 = Label(root,text="Username").grid(row=1,column=1)
# l2 = Label(root,text="Email").grid(row=2,column=1)
# l3 = Label(root,text="Phone").grid(row=3,column=1)


# t1 = Entry(root).grid(row=1,column=2)
# t2 = Entry(root).grid(row=2,column=2)
# t3 = Entry(root).grid(row=3,column=2)

# b1 = Button(root,text="submit").grid(row=4,column=2)




l1 = Label(root,text="Username").place(x=100,y=100)
l2 = Label(root,text="Email").place(x=100,y=150)
l3 = Label(root,text="Phone").place(x=100,y=200)


t1 = Entry(root).place(x=200,y=100)
t2 = Entry(root).place(x=200,y=150)
t3 = Entry(root).place(x=200,y=200)

b1 = Button(root,text="submit",width=15).place(x=200,y=250)

root.mainloop()