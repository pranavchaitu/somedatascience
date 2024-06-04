import pandas as pd

data1 = pd.Series({
    'a' : 100,
    'b' : 66,
    'd' : 69,
    'c' : 96
})

data2 = pd.Series({
    'a' : 4,
    'b' : 5,
    'd' : 6,
    'c' : 7
})

df = pd.DataFrame({
    "xirst" : data1,
    "second" : data2
})

# sorting rows then columns repectively
df.sort_index(inplace=True,ascending=True)
df.sort_index(axis=1,inplace=True)

print(df)

# print(df.iloc[0 : ])
# index object
index = df.index
# print(index[1])

# throws a error - index cant be changed
# index[1] = 'd' 

# df arangement
# df = pd.DataFrame(df,columns=['second','first'])
# print(df)


# # creating new column - derived
# df['sum'] = df['first'] + df['second']
# df['for90'] = df['first'] * 90 / 100 

# toppers = df[df['for90'] > 80]

# # to delete a column
# del df['sum']
# del toppers['sum']

# print(toppers)
# print(df)

# # indivual element access
# print(df.values[1,1])

# # accessing columns
# print(df.columns)
# print(df.T.columns)

