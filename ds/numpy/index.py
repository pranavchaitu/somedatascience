import numpy as np

# indexing and slicing

arr = np.arange(10)

# here they've been passed as reference and not as a copy
arr1 = arr

# to actually get a copy
# arr1 = arr.copy()

# before
print(arr == arr1)
arr1[5:8] = 12
# print(arr1)

# after
print(arr == arr1)

# to print all 
print(arr[:])
print(arr1[:])

# 2d indexing
arr = np.array([[1,2,3,4],[2,3,4,5]])
print(arr[1,2])
print(arr[1][2])
print(arr[1:,:2])

# 3d array and indexing

# arr3d = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
# print(arr3d.shape)
# print(arr3d[0][1][2])
# print(arr3d[0][1])