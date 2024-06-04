import pandas as pd 

data = pd.Series([1,2,3,4],index=['a','b','c','d'])

# other way using dict's
data = pd.Series({
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4
})

some = pd.Series([1,5,2,3])

print(some.describe())
# some.order()
# print(some)

# reindex
data = data.reindex(['b','c','d','a','e'])
# print(data)

data['a'] = 10

print(data.index)
print(data.values)
print(data)

# final included
print("\nafter silicing  'a' : 'c' ")
print(data['a' : 'c'])

# types
# print(type(data))
# print(type(data.index))
# print(type(data.values))
