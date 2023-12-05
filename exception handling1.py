try:
    a = 12/0
    print(a)
except Exception as e:
    print("Zero devision error...")
    print(e)
    
    
try:
    a = 12/0
    print(a)
except ZeroDivisionError as e:
    print("with error name...")
    print(e)