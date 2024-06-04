import numpy as np

# operation on arrays

data1 = [[1,2,3,4,3],[1,2.7,3,4,6]]
data2 = [[3,2,3,4,3],[1,2.7,3,4,5]]

arr1 = np.array(data1)
arr2 = np.array(data2)

arr3 = arr1 * arr2
arr3 = arr3.astype(np.int32)

print(arr3 * 100)

# arr = np.array(data,dtype=np.float32)

# # explicit data type conversion
# # converting floor int from float

# arr = arr.astype(np.int64)
# # arr = np.arange(22)
# print(arr.dtype)
# print(arr)


# print(arr.shape)
# print(arr.dtype)
# print(arr)