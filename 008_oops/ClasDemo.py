
class Pen:

   

    #data memeber / variables /state
    price=20
    color = "Red"
    

    def __init__(self):
        print("init calling")

    #function memeber / funcion  / methods
    def test(self):
        print(self.price,self.color,self.company)
        print("Test calling...")

p1 = Pen()
p1.company="SS"
p1.test()

p2 = Pen()
p2.test()