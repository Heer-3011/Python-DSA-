from os import *
from sys import *
from collections import *
from math import *

def countBits(n):
    bin1=int(bin(n)[2:])
    count=0
    while bin1!=0:
        rem=bin1%10
        if rem==1:
            count+=1
        bin1=bin1//10

    return count
n = int(input())
print(countBits(n))

