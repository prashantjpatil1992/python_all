class Chicken:
    def bird(self):
        print("Chicken can fly but not like others birds")
        

class Eagle(Chicken):
    def bird(self):
        print("Eagle can fly on very much hike")
        
        
obj = Eagle()
obj.bird()

