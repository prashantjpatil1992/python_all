def rec(n):
    print(n)
    n+=2
    if n<=20:
        return rec(n)
rec(2)
