class A:
    def __init__(self):
        self.__balance = 5000
        
    def showb(self):
        print(f"Your Account Balance Is {self.__balance}")

class B(A):
    def showd(self):
        print(self.__balance)
        
obj = B()
obj.showd()