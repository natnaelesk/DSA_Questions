def volodya_number(n,k):
    odd = []
    even = []
    for i in range(1,n+1):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    total = odd + even
    return total[k-1]


print ( volodya_number(10,3))
print ( volodya_number(7,7))