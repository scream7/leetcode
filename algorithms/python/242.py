class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        if len(s) != len(t):
            return False
        for cs,ct in zip(s,t):
            if cs not in dic.keys():
                dic[cs] = 1
            else:
                dic[cs] += 1
            if ct not in dic.keys():
                dic[ct] = -1
            else:
                dic[ct] -= 1
        
        for key in dic.keys():
            if dic[key]!=0:
                return False
        return True
