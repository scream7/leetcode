# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n + 1
        while low < high:
            num = (low + high) / 2
            res = guess(num)
            if res == 0:
                return num
            elif res == -1:
                high = num
            else:
                low = num + 1
        return num
                
