passw = input()
arr = []
n = int(input())
for _ in range(n):
    arr.append(input())

ans= [False,False]    
for i in arr:
    l = i[0]
    r = i[1]
    if i == passw:
        ans = [True,True]
    if l == passw[1]:
        ans[1] = True
    if r == passw[0]:
        ans[0] = True
        
if ans[1] & ans[0]:
    print("YES")
else:
    print("NO")