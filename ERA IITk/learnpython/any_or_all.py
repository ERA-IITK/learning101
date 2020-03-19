n=int(input())
x=list(input().split())
print(any(list(map(lambda s: s==s[::-1],x))) and all(list(map(lambda s: int(s)>0,x))))

