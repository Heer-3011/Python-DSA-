class Solution:
    def removeDuplicates(self, arr):
        arr_result=[]
        for i in range(0,len(arr)): 
                if arr[i] not in arr_result:
                    arr_result.append(arr[i]) 
        return arr_result

s1=Solution()
print(s1.removeDuplicates([1, 2, 2, 3, 4, 4, 4, 5, 5]))
print(s1.removeDuplicates([2,2,2,2]))
print(s1.removeDuplicates([1,2,3]))