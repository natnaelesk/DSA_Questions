#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        dic_a = dict(Counter(a))
        dic_b = dict(Counter(b))

        for (key, val) in dic_b.items():
            if key in dic_a:
                if val > dic_a[key]:
                    return False
            else:
                return False
        return True
    
    
