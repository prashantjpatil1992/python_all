sub=["Math","Physics","Chemistry","Biology"]
a=[70,88,44,61]
b=[40,50,70,70]
c=[88,90,50,40]

c[3]=80

name1="a"
i=0
c=a
total=0
while i<len(sub):
    if name1 == "a":
        print(sub[i], "=", c[i])
        total = total+c[i] 
    i+=1
    
re = (total/400)*100
print("total",total)
print("result in percent",re)




