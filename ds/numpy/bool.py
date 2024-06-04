# num = np.random.randint()
# print(num)
# important

import numpy as np

# boolean indexing
where = np.arange(6)
arr2 = np.array(["p","r","a",'n','a','v'])

# print(where)
print(where[arr2 == "x"])
print(where[arr2 == "a"])

data = np.array([1,3,-1,-11,33])
negative = data[data < 0] 
postive = data[data > 0] 

# separting 
print(negative)
print(postive)

# we can also do - here converting -ve's to 0 and +ve's to 1
# data[data < 0] = 0
# data[data > 0] = 1
# can also
data[data != 3] = 0
print(data)

# fancy indexing
arr = np.empty((4,4))
for i in range(4):
    arr[i] = i
print(arr)

print('---------------------------')
# conditional logic in numpy
xarr = np.array([3,3,3,3,3])
yarr = np.array([1,1,1,1,1])
zarr = np.array([True,False,True,False,False])
print([(x if c else y) for x,y,c in zip(xarr,yarr,zarr)])

#np.where condition usecase 
some = np.where(xarr > yarr,1,0)
print(some)

# bool methods - any true ? & all true ?
print(zarr.any())
print(zarr.all())

# filtering uniques
arr = np.unique(["pranav","chaitu","surya","surya"])
# arr = np.unique([1,1,2,2,3,4])
print(arr)

# alternative py code
arr2 = sorted(set(["pranav","chaitu","surya","surya"]))
print(arr2)