import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])

sum=arr1+arr2
print(sum)
 
#using np dot  operator
print("usinfg numpy.dot")
r1=np.dot(arr1,arr2)

print(r1)

#product of matrice
a = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
b= [ele for sub in a for ele in sub ]
print(b)
print(np.prod(b))

#addition
print( "Addition=")
print(np.add(arr1,arr2))

#subtract
print("Subtract=")
print(np.subtract(arr2,arr1))

#transpose
print(arr1.T)