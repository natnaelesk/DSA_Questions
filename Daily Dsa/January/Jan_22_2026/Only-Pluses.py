def maximum_bananas(a,b,c):
    arr = [a,b,c]
    for i in range(1,6):
        arr.sort()
        arr[0]+=1
    ans = 1
    for k in arr:
        ans*=k
    return ans




print(maximum_bananas(2,3,4))
print(maximum_bananas(10,1,10))