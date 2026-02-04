class Solution(object):
    def missingNumber(self, nums):
        total = sum(range(0,len(nums)+1))
        actual = sum(nums)
        return total - actual
        
        