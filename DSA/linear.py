# You are given an array ‘arr’ containing ‘n’ integers. You are also given an integer ‘num’,
#  and your task is to find whether ‘num’ is present in the array or not. 
# If ‘num’ is present in the array, return the 0-based index of the first occurrence of ‘num’. 
# Else, return -1. 
# Example:
# Input: ‘n’ = 5, ‘num’ = 4 
# 'arr' =  [6,7,8,4,1] 

# Output: 3
def linearSearch(n: int, num: int, arr: [int]) -> int:  
    for i in range(0,n,1): 
        if arr[i]==num:
            return i 
    return -1
 
arr =  [6,7,8,4,1]         
print(linearSearch(5,4, arr))    
#print(arr.index(4))
