class Chicken:
    def bird(self):
        print("Chicken can fly but not like others birds")
        

class Eagle():
    def bird(self):
        print("Eagle can fly on very much hike")
        
obj1 = Chicken()     
obj2 = Eagle()


for b in (obj1,obj2):
    b.bird()
    


