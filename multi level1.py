class Grand:
    def __init__(self):
        self.a = ["abc","efg","hij",1,3,4,5,6,7,8,9]
        
class Parent(Grand):
    def show(self):
        print("I am parent data")
        for i in range(4):
            print(self.a[i])
            
class Child(Parent):
    def cshow(self):
        print("I am a child data")
        for i in range(4,len(self.a)):
            
            print(self.a[i])
            
obj = Child()
obj.show()
obj.cshow()