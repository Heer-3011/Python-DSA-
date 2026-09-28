# Input: arr[] = [2, 2, 3, 1, 3, 2, 1, 1]
# Output: [1, 2]
# Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3 = 2).

# Input: arr[] = [-5, 3, -5]
# Output: [-5]
# Explanation: The frequency of -5 is 2, which is more than floor n/3 (3/3 = 1).

# Input: arr[] = [3, 2, 2, 4, 1, 4]
# Output: [ ]
# Explanation: There is no majority element.
def majority(arr):
    n=int(len(arr)/3)
    result=[]
    for i in range(0,len(arr)):
        count=0
        for j in range(0,len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count>n:
            result.append(arr[i])
    return list(set(result))

arr= [2, 2, 3, 1, 3, 2, 1, 1]
print(majority(arr))
arr=[3, 2, 2, 4, 1, 4]
print(majority(arr))
arr= [-5, 3, -5]
print(majority(arr))
