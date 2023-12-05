aa={'name': 'ABC', 'age': 25, 'City': 'Thane', 'Education': 'BTech', 'Job': 'Engineer'}

'''
print(aa.values())
for i in aa:
    keys.append(i)
    values.append(aa[i])
print(keys)
print(values)
'''

keys=["a"]
keys[0]="NAME"
print(keys)



keys=[1,2,3,4,5]
values=[1,2,3,4,5]
j=0
for i in aa:
    keys[j]=i
    values[j]=aa[i]
    j+=1
    
print(keys)
print(values)
        
 
