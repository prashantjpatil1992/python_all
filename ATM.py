for count in range(1,4):
    pin = int(input("Enter your pin :"))
    inquiry = input("what do you wanna do :")


    if inquiry == "inquiry" or inquiry =="Inquiry" or inquiry == "INQUIRY":
        print("5000000")
    
    if pin==1900:
        amount = int(input("enter amount"))
        if amount%100==0:
            if amount>=2000:
                notes = amount//2000
                print("2000 notes are :-", notes)
                amount = amount%2000
                if amount==0:
                    break
            if amount>=500:
                notes = amount//500
                print("500 notes are :- ",notes)
                amount = amount%500
                if amount==0:
                    break
            if amount>=200:
                notes = amount//200
                print("200 notes are :- ",notes)
                amount = amount%200
                if amount==0:
                    break
            if amount>=100:
                notes = amount//100
                print("100 notes are :-",notes)
                amount = amount%100
                if amount==0:
                    break
           
        else:
            print("Amount should be multiple of 100")
            break
    else:
        
        print("Wrong Password...")

else:
    print("Your Account Block For Next 24 hours")
print("Thank You Visit Agaian....")
        
