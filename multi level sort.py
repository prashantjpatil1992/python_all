class Data:
    def __init__(self):
        self.a = [100,22,33,10,70,60,55,21,11,400,420]
        
class Sort(Data):
    def sort(self):
        for i in range(len(self.a)):
            for j in range(len(self.a)):
                if self.a[i]<=self.a[j]:
                    r = self.a[i]
                    self.a[i] = self.a[j] 
                    self.a[j] = r
        print(self.a)
        
class Average(Sort):
    def avg(self):
        c=0
        for i in self.a:
            c=c+i
        avg1 = c/(len(self.a))
        print(f"Average value from lis is {avg1}")

class Max(Average):
    def max1(self):
        print(f"Maximum nu,ber from list is {self.a[-1]}")
    
    
    
        
obj = Max()
obj.sort()
obj.max1()
obj.avg()