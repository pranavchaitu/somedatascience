# random values
# data processing - np.meshgrid

import numpy as np

arr = np.random.randn(6)
np.sort(arr)
print(arr)

# sorted to sort
# three ways to sort
print(sorted([4,3,2,6]))
# returns None
print([4,3,2,6].sort())
print(np.sort([4,3,2,6]))