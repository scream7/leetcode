class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if n <= 0:
            return False
        res = math.log10(n)/math.log10(3)
        return (True if math.ceil(res) == float(res) else False)
        
