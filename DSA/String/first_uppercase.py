# Problem statement
# You are given a string 'STR'. You have to convert the first alphabet of each word
# in a string to UPPER CASE.

# For example:

# If the given string 'STR' = ”I am a student of the third year”
# so you have to transform this string to ”I Am A Student Of The Third Year"

from os import *
from sys import *
from collections import *
from math import *

def convertString(str):
    return upper(str)

print(convertString("This is prohgram"))