def pattern(*a):
    for row in range(len(a)):
        for col in range(len(a)):
            if (row==0) or (col%4==0 and row!=0) or (row==4):
                print(a[row], end=" ")
            else:
                print(" ",end=" ")
        print()

pattern("a","*","*","*","a")
