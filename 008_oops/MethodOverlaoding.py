from multipledispatch import dispatch

class Calc:

    @dispatch(int, int, int)
    def add(self,a,b,c):
        print(f"Addtio is {a+b+c}")

    @dispatch(int, int)
    def add(self,a,b):
        print(f"Addtio is {a+b}")

    # def add(self,*a):
    #    sum = 0
    #    for i in a:
    #        sum+=i
    #    print(sum)

c = Calc()
c.add(100,25,36)
c.add(10,20)