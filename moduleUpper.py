def Upper(aa):
    a = list(aa)
    for i in range(len(a)):
        if a[i]=="a":
            a[i]="A"
        if a[i]=="b":
            a[i]="B"
        if a[i]=="c":
            a[i]="C"
        if a[i]=="d":
            a[i]="D"
    return "".join(a)
            
            
def Lower(aa):
    a = list(aa)
    for i in range(len(a)):
        if a[i]=="A":
            a[i]="a"
        if a[i]=="B":
            a[i]="b"
        if a[i]=="C":
            a[i]="c"
        if a[i]=="D":
            a[i]="d"
    return "".join(a)
            
       