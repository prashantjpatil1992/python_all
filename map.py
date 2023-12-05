a=[1,2,3,4,5]
'''
def seq1(n):
    return n*2

b = map(seq1,a)

print(list(b))
'''

b = map(lambda n:n*4, a)
print(list(b))
