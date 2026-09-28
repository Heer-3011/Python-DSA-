# Input: arr[] = [1, 4, 5, 3, 7, 9]
# Output: 6
# Explanation: The strictly increasing subarrays are:
#  [1, 4], [1, 4, 5], [4, 5], [3, 7], [3, 7, 9], [7, 9]

# Input: arr[] = [1, 3, 3, 2, 3, 5]
# Output: 4
# Explanation: The strictly increasing subarrays are: [1, 3], [2, 3], [2, 3, 5], [3, 5] 

# Input: arr[] = [2, 2, 2, 2]
# Output: 0
# Explanation: No strictly increasing subarray exists.

def increasing_subarray(arr):
    subarray=[]
    
    for i in range(0,len(arr)-1):
        if arr[i]<arr[i+1]:
            subarray.append([arr[i],arr[i+1]]) 

    for i in range(0,len(arr)-2):
            if arr[i]<arr[i+1]<arr[i+2]:
                subarray.append([arr[i],arr[i+1],arr[i+2]]) 
    # print(subarray)
    return len(subarray)

arr=[1,4,5,3,7,9]
print(increasing_subarray(arr))
arr= [1, 3, 3, 2, 3, 5]
print(increasing_subarray(arr))
arr=[2, 2, 2, 2]
print(increasing_subarray(arr))