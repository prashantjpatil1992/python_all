for row in range(0,5):
    for col in range(0,4):
        if (row==0 and col%3!=0) or (row!=0 and col%3==0) or (row==2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
            
