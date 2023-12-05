class Grandparent:
    def __init__(abs,home, car, iphone, plote):
        abs.home = home
        abs.car = car
        abs.iphone = iphone
        abs.plote = plote
        
class Parent(Grandparent):
    def __init__(abs, home, car, iphone, plote,pcar="nnnn"):
        Grandparent.__init__(abs,home, car, iphone, plote)
        abs.pcar = pcar
    def pshow(abs):
        print(f"My Parent Gifted me {abs.home}")
        print(f"I have my own {abs.pcar}")
        
class Child(Parent):
   
    def cshow(abs):
        print(f"My grand pa gifted me {abs.iphone}")
        
obj = Child("Big House", "Nano Car", "iphone 15", "2 acrs of land")
obj.pshow()
obj.cshow()
    
        