import numpy as np

# shaping a  array
arr = np.arange(30).reshape((5,6))
print(arr)
print(arr.T)

# reordering axes
arr = np.arange(16).reshape((2,2,4))
print(arr)
arr1 = arr.transpose((1,0,2))
print(arr1 == arr)

