s=input()
count=1
s=s+' '
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        print("({}, {})".format(count,s[i-1]),end=" ")
        count=1
