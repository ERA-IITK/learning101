def print_formatted(number):
    for i in range(1,n+1):
        octal=oct(i)
        hexa=hex(i)
        binary=bin(i)
        print(i,end=" "*n)
        print(octal[2:],end=" "*n)
        print(hexa[2:],end=" "*n)
        print(binary[2:],end=" "*n)
        print()
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)