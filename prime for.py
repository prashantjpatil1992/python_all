a = int(input("Enter number :-"))
for i in range(2,a,1):
    r = a%i
    if r==0:
        print("This is not prime number")
        break
else:
    print("This is prime number")
