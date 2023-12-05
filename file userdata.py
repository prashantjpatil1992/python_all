filename = input("Create File With Your Name : ")
f = open(f"files/{filename}.txt",'x')
print("File Created")
name = input('Enter Your Name : ')
age = input("Enter Your Age : ")

w = open(f"files/{filename}.txt","w")
w.write(f"Name : {name} \n Age :{age}")


print("Data Entered Successfully")
