dict3 = {"a":1,"b":22,"c":2,"d":3,"e":2,"f":78}
print(dict3.values())
print(dict3.keys())
print(dict3.items())

dict3["Name"]="ABC"
dict3["f"] = "FFFFFFF"
print(dict3)


for i in dict3:
    print(i,"=", dict3[i])
   
