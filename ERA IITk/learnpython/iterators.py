from itertools import combinations

if __name__=='__main__':
    n=int(input())
    l=list(input().split())
    k=int(input())
    loi=[]
    for i in range(len(l)):
        if l[i]=='a':
            loi.append(i+1) 
    lis=list(range(1,n+1))
    comb=list(combinations(lis,k))
    total=len(comb)
    count=0
    for i in loi:
        for j in range(total):
            if i in comb[j]:
                comb[j]=[]
                count+=1
    print(count/total)
