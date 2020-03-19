#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    a=[]
    def takeFirst(lis):
        return lis[0]
    for i in range(97,123):
        ch=chr(i)
        count=0
        for j in s:
            if j==ch:
                count=count+1
        if count>=1:
            a.append([count,ch])
    sorta=sorted(a,key=takeFirst,reverse=True)
    count=0
    for i in sorta:
        print(i[1],end=" ")
        print(i[0])
        count=count+1
        if count==3:
            break


    
    

