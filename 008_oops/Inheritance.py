#super - parent - base
class Pen:

    def __init__(self,price,color,company):
        self.price = price
        self.color = color
        self.company = company

    def to_write(self):
        print(self.price,self.color,self.company)

#sub - child - derived
class Notebook(Pen):

    def __init__(self, price, color, company,pages):
        self.pages = pages
        super().__init__(price, color, company)


    def disaply(self):
         print(self.price,self.color,self.company,self.pages)

#multiple 
# class C(Pen,Notebook):
#     pass

#miltilvel
# class C(Notebook):
#     pass

#Hierarchical
# class C(Pen):
#     pass

p = Pen(10,"Red","ss")
p.to_write()

n = Notebook(11,"Black","Cello",100)
n.disaply()