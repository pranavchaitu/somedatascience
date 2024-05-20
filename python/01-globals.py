# 01-global varaibles
arr = [1,2,4]
i = 0
res = 0
while i < len(arr) :
    res += arr[i]
    i += 1

#---------------------------------------------------------------

def fun():
    global res
    res = "heheh"
    #calling global variable and manipulating it

print(res)
fun()
print(res)