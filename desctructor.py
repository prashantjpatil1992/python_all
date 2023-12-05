class A:
    def __init__(self):
        print("I will Exicute first")
    
    def __del__(self):
        print("i will delete the object")
        
    def show(self):
        print("proccessing........1")
        
    def show1(self):
        print("proccessing........2")
        
    
        
obj = A()
obj.show()
obj.show1()