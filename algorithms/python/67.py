class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        idx = 0
        carry = 0
        res = ""
        while idx < max(len(a),len(b)) or carry!=0:
            da = int(a[-1-idx]) if idx < len(a) else 0
            db = int(b[-1-idx]) if idx < len(b) else 0
            d = da + db + carry
            carry = d / 2
            d %= 2
            res += str(d)
            idx += 1
        return res[::-1]
                
obj = Solution()
print obj.addBinary("1","1")
