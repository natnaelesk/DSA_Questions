class Solution(object):
    def longestCommonPrefix(self, strs):
        stack = strs[0]
        for i in range(1,len(strs)):
            c = len(strs[i])
            for j in range(len(stack)):
                if j >= c:
                    stack = stack[:j]
                    break
                if strs[i][j] != stack[j]:
                    if j == 0:
                        return ""
                    stack = stack[:j]
                    break
        return stack