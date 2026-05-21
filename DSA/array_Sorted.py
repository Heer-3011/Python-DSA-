def is_sorted(arr):
    for i in range(1,len(arr)+1):
        if arr[i+1]<arr[i]:
            return False
        else:
            return True
print(is_sorted([1,9,2,3,4]))