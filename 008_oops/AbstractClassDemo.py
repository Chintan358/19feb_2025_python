from abc import ABC,abstractmethod

class Abs(ABC):

    @abstractmethod
    def display(self):
        pass

class AbsImpl(Abs):

    def display(self):
        print("display calling")

a = AbsImpl()
a.display()