#  sort the rows by the 2nd column so that we get:
# [[6, 1, 4],
# [8, 3, 2],
# [3, 6, 5]]
import numpy as np
arr = np.array([[8, 3, 2],
          [3, 6, 5],
          [6, 1, 4]])
#sort the array using np.sort
arr = np.sort(arr.view('i8,i8,i8'),
       order=['f1'],
       axis=0).view(int)

print(arr)

# reverse the array
reverse=arr[::-1]
print(reverse)

#shape of the array
print("\nShape of the array :",arr.shape)
 
 #creation of narray 
ndArray = np.array([[1, 2, 3, 4,2,3],[2,3,4,5,7,8]], ndmin=3)
print(ndArray)
print('Dimensions of array:', ndArray.ndim) 