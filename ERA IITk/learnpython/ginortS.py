x=input()
upper=list(filter(lambda x: x.isalpha() and x.isupper(),list(x)))
lower=list(filter(lambda x: x.isalpha() and x.islower(),list(x)))
even=list(filter(lambda x: x.isdigit() and int(x)%2==0,list(x)))
odd=list(filter(lambda x: x.isdigit() and int(x)%2!=0,list(x)))
upper.sort()
lower.sort()
even.sort()
odd.sort()
lis=lower+upper+odd+even
for i in lis:
    print(i,end="")
