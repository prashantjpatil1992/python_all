'''
a=[]
b=[]
for i in range(1,100):
    r=i%2
    if r==0:
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)
'''

lc = [x for x in range(1,101,2)]
print(lc)

lc1 = [i for i in range(1,101) if i%2==0]
print(lc1)

lc2 = [i*j for i in range(1,11) for j in range(11,11)]
print(lc2)
