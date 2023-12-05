class A:
    def __init__(self,__name,_age):
        
        self.__name = __name 
        
        self._age = _age
    def show(self):
        print(f"My name is {self.__name} and my age is {self._age}")
        
obj = A("AA",33)
obj.__name="Rohit"
obj._age = 24
obj.show()