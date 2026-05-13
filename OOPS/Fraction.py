from os import *
from sys import *
from collections import *
from math import *
from fractions import Fractions
class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator

    def add(self,obj1):
        f1=Fractions(self.numerator,self.denominator)
        f2=Fractions(obj1.numerator,obj1.denominator)
        f=f1+f2
        self.numerator