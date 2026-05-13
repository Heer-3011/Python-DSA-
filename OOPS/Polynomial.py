from os import *
from sys import *
from collections import *
from math import *

from copy import deepcopy

class Polynomial:
    
    def __init__(self):
        self.degCoeff = [0] * 10
        self.size = 10

    def setCoefficient(self, degree, coeff):

        if degree >= self.size:

            newSize = degree + 1
            newArr = [0] * newSize

            for i in range(self.size):
                newArr[i] = self.degCoeff[i]

            self.degCoeff = newArr
            self.size = newSize

        self.degCoeff[degree] = coeff

    def __add__(self, p):

        result = Polynomial()

        maxSize = max(self.size, p.size)

        result.degCoeff = [0] * maxSize
        result.size = maxSize

        for i in range(maxSize):

            a = 0
            b = 0

            if i < self.size:
                a = self.degCoeff[i]

            if i < p.size:
                b = p.degCoeff[i]

            result.degCoeff[i] = a + b

        return result

    def __sub__(self, p):

        result = Polynomial()

        maxSize = max(self.size, p.size)

        result.degCoeff = [0] * maxSize
        result.size = maxSize

        for i in range(maxSize):

            a = 0
            b = 0

            if i < self.size:
                a = self.degCoeff[i]

            if i < p.size:
                b = p.degCoeff[i]

            result.degCoeff[i] = a - b

        return result

    def __mul__(self, p):

        result = Polynomial()

        newSize = self.size + p.size

        result.degCoeff = [0] * newSize
        result.size = newSize

        for i in range(self.size):
            for j in range(p.size):

                result.degCoeff[i + j] += (
                    self.degCoeff[i] * p.degCoeff[j]
                )

        return result

    def print(self):

        for i in range(self.size):

            if self.degCoeff[i] != 0:
                print(str(self.degCoeff[i]) + "x" + str(i), end=" ")

        print()


def run():
    count1 = int(input())

    degree1 = list(map(int,input().split()))

    coeff1 = list(map(int,input().split()))


    first = Polynomial()
    for i in range(count1):
        first.setCoefficient(degree1[i], coeff1[i])

    count2 = int(input())


    degree2 = list(map(int,input().split()))

    coeff2 = list(map(int,input().split()))


    second = Polynomial()
    for i in range(count2) :
        second.setCoefficient(degree2[i], coeff2[i])


    choice = int(input())

    result = Polynomial()

    if choice == 1:
        result = first + second
        result.print()

    elif choice == 2:
        result = first - second
        result.print()

    elif choice == 3:
        result = first * second
        result.print()

    elif choice == 4:
        third = deepcopy(first)

        if (third.degCoeff == first.degCoeff):
            print("true")
        else:
            print("false")

    else:
        fourth = deepcopy(first)

        if (fourth.degCoeff == first.degCoeff):
            print("true")
        else:
            print("false")


run()