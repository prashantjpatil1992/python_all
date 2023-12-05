class HR:
    def __init__(self,amount):
        self.amount = amount
        
class employee1(HR):
    def growth1(self,payemnt):
        
        print(f"I am employee1 have {payemnt} of salary and i got {self.amount} hike this year")
        
class employee2(HR):
    def growth2(self, payment):
        print(f"I am employee2 {payment} of salary and i got {self.amount} hike this year")
        

class employee3(employee1, employee2,HR):
    def growth3(self):
        print("i am employee3 and i exposing every one here")
        
obj = employee3("5%")
obj.growth1(40000)
obj.growth2(20000)

# obj1 = employee2("30%")
# obj1.growth2(20000)
