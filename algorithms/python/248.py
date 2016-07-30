class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        strnum = str(num)
        while len(strnum) > 1:
            sum = 0
            for c in strnum:
                sum += int(c)
            strnum = str(sum)
        return int(strnum)
