def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            if string[i:j]==sub_string:
                count=count+1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)