#f=open("files/fileFirst.txt","x")
 
# f=open("files/fileFirst.txt","w")
# f.write("Sorry bro we replace your previous data with thid=s")


f=open("files/fileFirst.txt","r")
#print(f.read())
line = f.readlines()
for i in range(1,3):
    print(line[i])

