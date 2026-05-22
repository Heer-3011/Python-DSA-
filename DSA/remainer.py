# Given an array of numbers and an integer n, 
# the task is to find the remainder when all numbers in the array are multiplied and divided by n.

# Examples:

# Input: arr[] = [100, 10, 5, 25, 35, 14],  n = 11
# Output: 9
# Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9
def remainder(arr,n):
    mul=1
    for i in range (0,len(arr)):
        mul*=arr[i]
    return mul % n
arr = [100, 10, 5, 25, 35, 14]
n = 11
print(remainder(arr,n))