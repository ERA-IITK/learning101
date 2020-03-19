def check(ch):
    if ch>='0' and ch<='9' or ch>='a' and ch<='z' or ch>='A' and ch<='Z':
        return True
    else:
        return False

s=input()
flag=True
for i in range(1,len(s)):
    if check(s[i]):
        if s[i]==s[i-1]:
            print(s[i])
            flag=False
            break
if flag:
    print("-1")
