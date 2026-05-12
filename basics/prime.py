from os import *
from sys import *
from collections import *
from math import *

# Function to check prime
def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# Function to count total primes
def totalPrime(s, e):
    count = 0

    for i in range(s, e + 1):
        if isPrime(i):
            count += 1

    return count


# Taking input
S, E = map(int, input().split())

print(totalPrime(S, E))