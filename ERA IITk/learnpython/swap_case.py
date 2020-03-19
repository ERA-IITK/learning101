def swap_case(s):
    l=""
    for i in s:
        if i>='a' and i<='z':
            l=l+chr(ord(i)-32)
        elif i>='A' and i<='Z':
            l=l+chr(ord(i)+32)
        else:
            l=l+i  
    return l

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)