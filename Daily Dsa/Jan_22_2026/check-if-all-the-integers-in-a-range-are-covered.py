class Solution(object):
    def isCovered(self, ranges, left, right):
        my_range=range(left,right+1)
        for i in ranges:
            j=0
            while j < len(my_range):
                if my_range[j] in range(i[0] , i[1]+1):
                    my_range.pop(j) 
                    continue
                j+=1
        return True if (len(my_range) == 0) else False
        