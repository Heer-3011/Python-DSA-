# input arr={1,2,3,4,5,6},d=2
# output= {5,6,1,2,3,4}

def rotation(arr,d):
    print(-d)
    for i in range(-d,0,-1):
        print(arr[i])

arr=[1,2,3,4,5,6]
# print(arr[-2])
# print(rotation(arr,2))
rotation(arr,2)