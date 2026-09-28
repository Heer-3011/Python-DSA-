# # Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
# # Output: 1
# # Explanation: Element 1 appears 4 times. Since ⌊7/2⌋ = 3, and 4 > 3,
# #  it is the majority element.
# Input: arr[] = [2, 13]
# Output: -1
# Explanation: No element appears more than ⌊2/2⌋ = 1 time,
#  so there is no majority element.

def majority(arr):
    n=int(len(arr)/2)
    
    for i in range(0,len(arr)):
        count=0
        for j in range(0,len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count>n:
            return arr[i]
    return -1

arr= [1, 1, 2, 1, 3, 5, 1]
print(majority(arr))
arr=[1,2,3]
print(majority(arr))

