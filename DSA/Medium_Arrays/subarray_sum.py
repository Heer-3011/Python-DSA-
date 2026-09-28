# nput: arr[] = [1, 4, 5, 3, 2]
# Output: 116
# Explanation: Sum of all possible subarrays of the array [1, 4, 5, 3, 2] is 116.

# Input: arr[] = [1, 2, 3, 4]
# Output: 50
# Explanation: Sum of all possible subarrays of the array [1, 2, 3, 4] is 50

def subarraySum(arr):
    n = len(arr)
    result = 0 
    for i in range(n):
        temp = 0 
        for j in range(i, n):  
            temp += arr[j]
            result += temp
    return result

arr = [1, 4, 5, 3, 2]
print(subarraySum(arr))
arr=[1,2,3,4]
print(subarraySum(arr))