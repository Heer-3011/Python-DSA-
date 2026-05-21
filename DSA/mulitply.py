# Input: arr[] = [2, 4, 5]
# Output: [8, 40, 20] 
def mulitply_adjacent(arr):
    result_arr=[]
    for i in range(0,len(arr) ):
        if i==0:
            result_arr.append(arr[i]*arr[i+1])
        elif i==len(arr)-1:
            result_arr.append(arr[i-1]*arr[i])  
        else:  
            result_arr.append(arr[i-1]*arr[i]*arr[i+1])
    return result_arr  
   
arr=[2, 4, 5]  
print(mulitply_adjacent(arr))
arr2 = [2, 5, 7, 8, 3]
print(mulitply_adjacent(arr2))
 
