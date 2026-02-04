def maximum_bananas(a,b,c):
    arr = [a,b,c]
    for i in range(1,6):
        arr.sort()
        arr[0]+=1
    ans = 1
    for k in arr:
        ans*=k
    return ans

test_cases = int(input())
for _ in range(test_cases):
         str = input()
         str = str.split()
         print( maximum_bananas(int(str[0]),int(str[1]),int(str[2])))
         