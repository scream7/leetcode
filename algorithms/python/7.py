class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return x
        sign = 1 if x > 0 else -1
        x = abs(x)
        res = 0
        while x:
            res *= 10
            res += x%10
            x /= 10
        if res > 2**31 + 1 or res < -2**32 - 1:
            return 0
        return res * sign
        