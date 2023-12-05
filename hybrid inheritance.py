class ITV:
    def __init__(self,name):
        self.name = name
        
class Student1(ITV):
    def admission(self):
        print(f"Admission Confirm in {self.name}")
        
class Student2(ITV):
    def admission1(self):
        print(f"Admission confirm in {self.name}")
        
class Student3(Student1, Student2,ITV):
    def admission3(self):
        print("Decision pending....")
        
obj = Student3("IT Vedant")
obj.admission()
obj.admission1()
obj.admission3()
        
        
        