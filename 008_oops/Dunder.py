# class Demo:

#     name = "krish"
#     def __init__(self):
#         print("Demo calling")

#     def __str__(self):
#         return self.name

# d =  Demo()
# print(d)



# class Calc:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def __eq__(self, value):
#         return self.a==value.a and self.b==value.b

# c1 = Calc(10,20)
# c2 = Calc(10,20)
# print(c1==c2)



class Sample:

    def __init__(self,a):
        self.a = a

    def __len__(self):
        return len(self.a)
    
    def __getitem__(self, key):
        return self.a[key]

    def __setitem__(self, key, value):
        self.a[key] = value
        


s = Sample([10,20,30,40,50])
# print(len(s))
s[1] = 1000
print(s[1])