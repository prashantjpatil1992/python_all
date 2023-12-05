class Parent:
    def __init__(self,home, car, iphone, plote):
        self.home = home
        self.car = car
        self.iphone = iphone
        self.plote = plote
    def show(self):
        print(f"I have {self.home}, {self.car}, {self.iphone} and {self.plote}")
        
        
class Child(Parent):
    def cshow(self):
        print(f" My Parent Gifted Me {self.iphone} and also {self.car}")
        
obj = Child("Big House", "Nano Car", "iphone 15", "2 acrs of land")
obj.cshow()
obj.show()
print(type(obj))
        