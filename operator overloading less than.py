class Less:
    def __init__(self,a):
        self.a = a
        # print(self.a)
        
    def __gt__(r,l):
        a = r.a>l.a
        return Less(a)
    
    def __str__(self):
        return f"{self.a} "
        
        
obj1 = Less(12)
obj2 = Less(100)
# obj3 = Less(123)
print(obj1>obj2)