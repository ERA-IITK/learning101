n=int(input())
for i in range(n):
    l=list(input().split())
    a=l[0]
    b=l[1]
    if not (b.isdigit() and a.isdigit()):
        try:
            print(int(a)/int(b))
        except ValueError as e:
            if not a.isdigit():
                print("Error Code: invalid literal for int() with base 10: '{}'".format(a))
            else:
                print("Error Code: invalid literal for int() with base 10: '{}'".format(b))
    elif int(b)==0:   
        try:
            print(int(a)/int(b))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
    else:
        print(int(int(a)/int(b)))
