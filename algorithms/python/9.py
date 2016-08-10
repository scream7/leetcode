class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        elif x < 10:
            return True
        else:
            strx = str(x)
            i = 0
            j = len(strx) - 1
            while i < j:
                if strx[i] != strx[j]:
                    return False
                i += 1
                j -= 1
            return True
        
