import math

def volodya_number(n,k):
    d= n/2
    d = math.ceil(d)
    if  k < d:
        #odd
        return k+2
    else:
        return k-d+3

s = input()
s = s.split()
print(volodya_number(int(s[0]),int(s[1])))



