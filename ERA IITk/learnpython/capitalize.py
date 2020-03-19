#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    p=list(" "+s);
    for i in range(len(p)):
        if p[i]==" ":
            if p[i+1].isalpha() and p[i+1].islower():
                p[i+1]=chr(ord(p[i+1])-32)
    x=""
    for i in range(1,len(p)):
        x=x+p[i]
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
