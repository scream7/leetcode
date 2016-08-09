class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        binary = bin(num)
        if binary[2] == '1' and len(binary) % 2 == 1 and '1' not in binary[3:]:
            return True
        else:
            return False
            
