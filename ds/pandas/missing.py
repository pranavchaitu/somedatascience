import pandas as pd

data1 = pd.Series({
    'a' : 100,
    'b' : 66,
    'c' : 69,
    'd' : 96
})

data2 = pd.Series({
    'a' : 4,
    'b' : 5,
    'c' : 6,
    'e' : 7
})

data3 = pd.Series({
    'a' : 8,
    'b' : 9,
    'c' : 10,
    'd' : 11,
    'e' : 12
})

df = pd.DataFrame([data1,data2,data3])

print(df)
print() 
df = df.fillna(0)
# newdf = df[df.isnull() == True]
print(df)
