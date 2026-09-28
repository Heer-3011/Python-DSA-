# Input: arr[] = [12, 11, 10, 5, 6, 2, 30]
# Output: 5, 6, 30
# Explanation: As 5 < 6 < 30, and they  appear in the same sequence in the array 

# Input: arr[] = [1, 2, 3, 4]
# Output: 1, 2, 3 
# Explanation: As 1 < 2 < 3, and they  appear in the same sequence in the array 

# Input: arr[] = [4, 3, 2, 1]
# Output: No such triplet exists.

def sorted_sub(arr):
    for i in range(0,len(arr)-2):
        for j in range(i,len(arr)-1):
            for k in range(j,len(arr)):
                if arr[i]<arr[j]<arr[k]:    
                    return arr[i],arr[j],arr[k]

arr= [1, 2, 3, 4]
print(sorted_sub(arr))
arr= [12, 11, 10, 5, 6, 2, 30]
print(sorted_sub(arr))