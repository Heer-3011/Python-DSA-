# Given an array and an integer k, the task is to split the 
# array from the kth position and move the first part to the end. For Example:

# Input: arr = [12, 10, 5, 6, 52, 36], k = 2  
# Output: [5, 6, 52, 36, 12, 10]
# Explanation: Split the array at index k and move the first part [12, 10] 
# (for k = 2) to the end.
def split(arr,k): 
    return arr[k:]+arr[:k]

arr=[12, 10, 5, 6, 52, 36]
k=3
print(split(arr,k)) 