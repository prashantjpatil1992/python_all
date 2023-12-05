a = [11,2,1,3,5,4,8,11,1,0]
c=0
for i in range(0,len(a),1):
    for j in range(0,len(a),1):
        if a[i]<=a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        print(c, a)
        c+=1