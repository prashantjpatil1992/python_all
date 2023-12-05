j=1
while j<=100:
    if j>1:
        i=2
        while i<j:
            r=j%i
            if r==0:
                break
            i+=1
        if j==i:
            print(j)
    j+=1
