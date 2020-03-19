if __name__ == '__main__':
    N = int(input())
    l=[]
    for _ in range(N):
        a=input()
        if a=="print":
            print(l)
        elif a=="sort":
            l.sort()
        elif a=="pop":
            l.pop()
        elif a=="reverse":
            l.reverse()
        else:
            x,*r=a.split()
            if x=="insert":
                l.insert(int(r[0]),int(r[1]))
            if x=="append":
                l.append(int(r[0]))
            if x=="remove":
                l.remove(int(r[0]))
