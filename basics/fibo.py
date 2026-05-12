from os import *
from sys import *
from collections import *
from math import *

def fibonacciNumber(n):
    if n <= 1:
            return n
    return fibonacciNumber(n - 1) + fibonacciNumber(n - 2)     

number=int(input()) 
for i in range(number):
    n=int(input())
    print(fibonacciNumber(n))
