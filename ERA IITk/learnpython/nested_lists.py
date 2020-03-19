if __name__ == '__main__':
    l=[]
    def second(lis):
        return lis[1]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    sortlist=sorted(l, key=second)
    secondlist=[]
    count=0
    for i in range(1,len(l)):
        if sortlist[i][1]!=sortlist[i-1][1]:
            count=count+1
        if count==1:
            secondlist.append(sortlist[i])
    sortlist2=sorted(secondlist)
    for i in sortlist2:
        print(i[0])
    
