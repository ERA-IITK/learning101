if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    for i in range(n):
        m=i
        for j in range(i+1,n):
            if l[j]>l[m]:
                m=j
        t=l[m]
        l[m]=l[i]
        l[i]=t
    for i in range(1,n):
        if l[i]!=l[i-1]:
            print(l[i])
            break
