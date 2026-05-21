# time complexity o(n)
def checking(arr):
    result=[]
    for i in range(1,len(arr),1):
        if arr[i] :
            result.append(i)
    return result        
arr=[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1]
print(checking(arr)) 

def check(arr,value):
    index=0+len(arr)//2
    if arr[index]==value:
        return index
    elif arr[index]>value:
        last=arr[index] 

arr1=[2,6,8,12,13,17]
print(check(arr1,6))