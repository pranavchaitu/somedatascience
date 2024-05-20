str = "hello,world"
for i in str :
    print(i)

# -------------------------------------------------------

if("hellow" in str):
    print("yes hello is there in hello world")

#just for the not in operator 
elif "hellow" not in str:
    print("No bro hello not present")

# -------------------------------------------------------

# start and last indices    
print(str[:-1])   
print(str.upper())
print(str.lower())

#trims extra space
print(str.strip())

#replaces char or a string
print(str.replace("hello","hi"))

#slplits at a comma encounter in the string
print(str.split(','))

#f strings
print(f'Hey your str (formatte)d = {str}')

#------------------------------------------------------
#PLACEHOLDERS AND MIDIFIERS - FORMATTING

num = 10
#fixing num to 2 fixed points
print(f'num = {num:.2f}')


