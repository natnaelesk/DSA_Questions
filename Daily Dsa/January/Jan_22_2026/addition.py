
def addition(s):
    if len(s) != 3:
        return None
    return int(s[0]) + int(s[2])

test_cases = int(input())
for _ in range(test_cases):
         str = input()
         print(addition(str))
         



