# for i in range(2,6):
#     print(i)

# print(type(1) == float)

# num1 = str(1)
# num2 = str(2)

# str1 = ""

# for i in range(1,5):
#     str1 = str1 + str(i)
# print(str1)

arr = [2,3,6,6,5]

max = 0
for i in arr:
    if i > max:
        max = i
max2 = 0
for i in arr:
    if i > max2 and i != max:
        max2 = i
print(max2)