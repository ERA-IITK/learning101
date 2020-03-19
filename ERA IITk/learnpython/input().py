h=list(map(int,input().split()))
n=h[0]
x=h[1]
lis1=[]
for i in range(x):
    h=list(map(float,input().split()))
    lis1.append(h)
lis2=zip(*lis1)
for i in lis2:
    print(sum(i)/x)
