class ATM:
    def cash(self):
        data = [2000,500,200,100]
        amount = 5300
        for i in range(len(data)):
            if amount%(data[len(data)-1])==0:
                if amount>=data[i]:
                    notes = amount//data[i]
                    print(f"{data[i]} of notes are {notes}")
                    amount = amount%data[i]
            else:
                print("Amount Should Be Multiple Of 100")
                break
                    
obj = ATM()
obj.cash()
