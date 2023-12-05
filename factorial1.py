def facto(fact,n):
    fact = fact*n
    n+=1
    if n<=5:
        return facto(fact,n)
    print(fact)
facto(1,1)
