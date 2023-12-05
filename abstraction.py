from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def abc(self):
        print("This is Abstraction method...")
        
    def abc1(self):
        print("Second abs")
        
class B(A):
    def abc(self):
        print("abstracte ................")
    def show(self):
        print("Not Abstracted...")
        
obj = B()
obj.show()
obj.abc1()
    