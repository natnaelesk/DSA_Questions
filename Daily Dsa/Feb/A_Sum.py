def sum(nums):
    if nums[0] + nums[1] == nums[2] or nums[2] + nums[1] == nums[0]  or nums[0] + nums[2] == nums[1] :
        return "YES"
    
    return "NO" 


n = int(input())
for _ in range(n):
    l= input()
    l= list(map(int , l.split()))
    print (sum(l))