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

s = input()
s =s.split()
print(volodya_number(int(s[0]),int(s[1])))



