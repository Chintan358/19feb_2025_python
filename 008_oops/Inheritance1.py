# class Animal:

#     def __init__(self,name,bread):
#         self.name = name
#         self.bread=bread

#     def display(self):
#         print(f"animal name is {self.name} and bread is {self.bread}")


# class Cat(Animal):
#     def __init__(self, name, bread):
#         super().__init__(name, bread)

# class Dog(Animal):
#     def __init__(self, name, bread):
#         super().__init__(name, bread)


# c = Cat("zenny","Parsian")
# c.display()

# d = Dog("Tommy","Labrado")   
# d.display()



class A :

    def __init__(self):
        print("A constructor")

    def display(self):
        print("Class A display calling")



class B :

    def __init__(self):
        print("B constructor")

    def display(self):
        print("Class B display calling")


class C(A,B):
    
    def __init__(self):
        B.__init__(self)

    def display(self):
        print("C display calling")
        B().display()


c = C()
c.display()



