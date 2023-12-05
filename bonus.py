exp = float(input("Enter how many years of experience do you have :-"))
salary = float(input("Please enter your monthly income/salary :-"))

if exp>=1 and exp<=3 and salary <=30000 and salary>=15000:
    print("Good news, you are eligible for full bonus")
    print("You will get this amount = ", salary+salary)
elif exp>3 and exp<=6 and salary>30000 and salary<=70000:
    print("Your bonus amount will be", salary+15000)
else:
    print("You are not eligible for bonus")
