def grp_reverse(arr,k):
    result_arr=[]
    if k>len(arr):
        return reverse(arr)
    for i in range(k+1):
        arr1=arr[:k]
        result_arr.append(reverse(arr1))
    return result_arr
def reverse(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr    

arr=[1,2,3,4] 
print(grp_reverse(arr,2))