def volodya_number(n, k):
    d = (n + 1) // 2   
    if k <= d:
        #odd
        return 2 * k - 1
    else:
        #Even 
        return 2 * (k - d)  

s = input()
s = s.split()

print(volodya_number(int(s[0]),int(s[1])))



