import textwrap

def wrap(string, max_width):
    p=""
    for i in range(len(string)):
        if i%max_width==0 and i!=0:
            p=p+"\n"+string[i]
        else:
            p+=string[i];
    return p

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)