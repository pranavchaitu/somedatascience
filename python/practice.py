def twoSum(arr, target):
    map = {}
    for i, num in enumerate(arr):
        comp = target - num
        if comp in map:
            return [map[comp],i]
        map[num] = i
    return []

def nextOdd(str):
    for i in range(len(str)-1,-1,-1):
        if(int(str[i]) % 2):
            return str[:i+1].lstrip('0')
    return ""

def main():
    arr_input = input()
    arr = list(map(int, arr_input.split()))
    target = int(input())
    print(twoSum(arr, target))

# main()
# print(twoSum([1,4,3,5],7)) # to result [1,2]

print(nextOdd('01256'))