def linear(arr,z):
    for i in range(0,len(arr)):
        if arr[i]==z:
            return f"Element found at index {i}"
    else:
        return "Element not found"

arr1= [10, 50, 30, 70, 80, 20, 90, 40]
x = 30
print(linear(arr1,x))