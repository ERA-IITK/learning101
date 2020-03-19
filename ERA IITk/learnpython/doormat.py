l=list(map(int,input().split()))
n=l[0]
m=l[1]
for i in range(n):
    if i==(n-1)//2:
        print('-'*((m-7)//2),end="")
        print("WELCOME",end="")
        print('-'*((m-7)//2))
    elif i<(n-1)//2:
        print("-"*((m-(2*i+1)*3)//2),end="")
        print(".|."*(2*i+1),end="")
        print("-"*((m-(2*i+1)*3)//2))
    else:
        x=n-i-1
        print("-"*((m-(2*x+1)*3)//2),end="")
        print(".|."*(2*x+1),end="")
        print("-"*((m-(2*x+1)*3)//2))