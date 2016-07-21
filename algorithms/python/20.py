class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 1:
            return False
        stack = []
        dic = {'[':']','{':'}','(':')'}
        res = True
        for c in s:
            if c in dic.keys():
                stack.append(c)
            elif c in dic.viewvalues():
                if len(stack) == 0 or dic[stack.pop()] != c:
                    return False
            else:
                return False
        res = True if len(stack)==0 else False
        return res

sol = Solution()
print sol.isValid('()')

