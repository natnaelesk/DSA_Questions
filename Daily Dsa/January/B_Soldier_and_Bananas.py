def borrow(k,n,w):
    total = 0
    for i in range(1,w+1):
        total += (k*i)
    return total-n if total > n else 0


s = input()
s =s.split()
print(borrow(int(s[0]),int(s[1]),int(s[2])))
         
