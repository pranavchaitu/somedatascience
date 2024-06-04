import pandas as pd 

data = pd.Series(['a','b','c','d'],index=[1,3,5,7])

# other way using dict's
data = pd.Series({
    1 : 'a',
    3 : 'b',
    5 : 'c',
    7 : 'd'
})

print()

# loc for explicit - our own indices
print(data.loc[1:5]) 

print()
# iloc for implicit - our own indices
print(data.iloc[1:5])