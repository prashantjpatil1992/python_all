a=[11,23,1,2,3,55,66,71,2,1,3]
dupli = []
c=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            c+=1
            dupli.append(a[j])
print(a)
print(dupli)
print(c)


            
