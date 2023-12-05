n=int(input("Enter number "))
a1=n
n1 = str(n)


count=0
for i in n1:
    count+=1
print(count)

sum1=0
while n!=0:
    sum1 = sum1+((n%10)**count)
    n=n//10
if a1==sum1:
    print("This is a armstrong number ")
else:
    print("This is not a armstrong number")
    
