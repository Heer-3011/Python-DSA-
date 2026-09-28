# Input: arr[] = [-2, 6, -3, -10, 0, 2]
# Output: 180
# Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.

# Input: arr[] = [-1, -3, -10, 0, 6]
# Output: 30
# Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.

def subarray_product(arr):
    res = arr[0] 

    for i in range(len(arr)):
        currpro = 1 
        for j in range(i, len(arr)):
            currpro = currpro * arr[j] 
            res = max(res, currpro)
    return res
 
arr = [-2, 6, -3, -10, 0, 2]
print(subarray_product(arr))
arr=[-1, -3, -10, 0, 6]
print(subarray_product(arr))
arr=[2, 3, 4] 
print(subarray_product(arr))