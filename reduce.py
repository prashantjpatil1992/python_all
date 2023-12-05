import functools
import operator

a=[1,2,3,4,5,6,7]
#b = functools.reduce(lambda a,b:a+b,a)
print( functools.reduce(lambda a,b:a+b,a))
print(functools.reduce(operator.add,a))


s=0
for i in range(len(a)):
    s=s+a[i]
print(s)

