for row in range(1,6):
    for col in range(1,4):
        if(row==1) or(row==5) or (row!=0 and col%2!=0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
