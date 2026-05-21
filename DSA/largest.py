from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    max=0
    for i in range(0,n) :
        if max<arr[i]:
            max=arr[i]
    return max

print(largestElement([1,2,333,4,5,0,2,100,3],9))