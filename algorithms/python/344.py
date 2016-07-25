class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in range(len(s)-1,-1,-1):
            res.append(s[i])
        return ''.join(res)
