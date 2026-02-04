def avr(s):
    if len(s) > 10:
        return s[0]+f"{len(s)-2}"+s[-1]
    return s

test_cases = int(input())
for _ in range(test_cases):
         str = input()
         print(avr(str))
         
