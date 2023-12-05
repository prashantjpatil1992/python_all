class Father:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
    
    def fshow(self):
        print("Father Class and my wife name is", self.mname)
        
class Mother: 
    def __init__(self,mname):
        self.mname = mname
    def mshow(self):
        print(f"Mother Class and our contact number is {self.contact}")
        
class Child(Mother, Father):                                                         
    def __init__(self,name,contact,mname):
        self.mname = mname
        Father.__init__(self,name,contact)
        Mother.__init__(self,mname)
    def cshow(self):
        print(f"I am a Child Class my father name is {self.name} and mother name is {self.mname}")
        
obj = Child("ABC",1234567891,"XYZ")
obj.fshow()
obj.mshow()
obj.cshow()