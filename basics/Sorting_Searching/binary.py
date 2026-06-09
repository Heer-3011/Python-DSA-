def binary_serach(arr,x):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=low +(high-low)//2
        if arr[mid] < x :
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

print(binary_serach([1,2,3],9))
