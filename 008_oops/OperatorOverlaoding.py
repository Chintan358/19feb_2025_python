class math: 

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a+other.a,self.b+other.b

    def __mul__(self, other):
        return self.a*other.a,self.b*other.b



m1 = math(10,20)
m2 = math(40,50)
k = m1*m2
print(k)