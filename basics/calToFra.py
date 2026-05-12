from os import *
from sys import *
from collections import *
from math import *
s=int(input())
e=int(input())
w=int(input()) 
for i in range(s,e+1,w):
    print(i,int((i- 32) * 5 / 9))  