def thirdLargest(arr):
    n = len(arr) 
    if n < 3:
        return -1 
    arr.sort() 
    return arr[n - 3]

if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    print(thirdLargest(arr))
    arr = [5,5,5]
    print(thirdLargest(arr)) 
    arr = [5,5,5,6]
    print(thirdLargest(arr))
    