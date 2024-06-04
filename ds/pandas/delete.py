import pandas as pd 

s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])

df = pd.DataFrame([s1,s1])
# print(df)

s1 = s1.drop(['c','d'])

# with column - a and row - 1 are deleted
# del df['a']

# inplace is used so that we wont store it again - wont return a object
df.drop(['a'],axis='columns',inplace=True)
df = df.drop([1],axis=0)

print(s1)
print(df)