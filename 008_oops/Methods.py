class Demo:

    id = 10

    def __init__(self,name):
        self.name=name

    def test(self):
        print(self.id,self.name)

    @classmethod
    def display(cls):
        print(cls.id)

    @staticmethod
    def run():
        print("run calling")


d = Demo("xyz")
d.test()
# d.run()

Demo.display()
Demo.run()