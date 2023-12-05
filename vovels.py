a="my name is rohit "
vovels = "aieou"
conso = "abcdfghjklmnpqrstvwxyz"
v=0
c=0
space=0
for i in a:
    if i in vovels:
        v=v+1
    elif i in conso:
        c+=1
    else:
        space+=1
        
        
print(f"Number of vovels are {v}")
print(f"Number of c are {c}")
print(f"number of spaces are {space}")
        
    
