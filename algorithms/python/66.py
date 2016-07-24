class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            d = digits[i]
            d += carry
            if d /10 == 1:
                d %= 10
                carry = 1
            else:
                carry = 0
            res.insert(0,d)
        if carry:
            res.insert(0,carry)
        return res
