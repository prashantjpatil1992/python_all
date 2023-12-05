dict1 = {'name':"abc", 'age':33, "":23232323, 1:"RRR"}
print(dict1)
print(dict1[""])
print(dict1[1])

dict2 = {"a":1,"b":22,"c":2,"d":3}
print(dict2['a']+dict2['b']+dict2['c']+dict2['d'])

sum1=0
for i in dict2:
    print(i)
    sum1 = sum1+dict2[i]
print(sum1)



