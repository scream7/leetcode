class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        ret = 0
        startidx = 0
        while str[startidx] == ' ':startidx += 1
        str = str[startidx:]
        positive = True
        if str[0] == '-':
            positive = False
            str = str[1:]
        elif str[0] == '+':
            positive = True
            str = str[1:]
        for c in str:
            if ord(c) in range(ord('0'),ord('9') + 1):
                ret *= 10
                ret += int(c)
            else:
                break
        ret = ret if positive else -ret
        if ret > 2**31-1:
            ret = 2**31-1
        elif ret < -2**31:
            ret = -2**31
        return ret

test = Solution()
print test.myAtoi('  -+2')

