def borrow(k,n,w):
    total = 0
    for i in range(1,w+1):
        total += (k*i)
    return total-n if total > n else 0


print ( borrow(3,17,4))