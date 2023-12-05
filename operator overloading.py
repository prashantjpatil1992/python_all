class Add:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        # print(self.a, self.b)
    
    def __add__(right,left):
        a = right.a+left.a
        b = right.b+left.b
        return Add(a,b)
    
    def __str__(self):
        return f"{self.a} {self.b}"
        
obj1 = Add(1,2)
obj2 = Add(3,4)
print(obj1+obj2)