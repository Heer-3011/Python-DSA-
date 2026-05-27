#interchange first and last value 
def interchange(arr):
    arr[0],arr[-1]=arr[-1],arr[0]
    return arr

print(interchange([1,2,3,4]))

