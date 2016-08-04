class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for pow,c in enumerate(s[::-1]):
            ans += (ord(c) - ord('A') + 1) * (26**pow)
        return ans
