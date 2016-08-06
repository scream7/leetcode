class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sdic = {c:None for c in s}
        tdic = {c:None for c in t}
        for cs,ct in zip(s,t):
            if sdic[cs] is None:
                sdic[cs] = ct
            if tdic[ct] is None:
                tdic[ct] = cs
            if sdic[cs] != ct or tdic[ct] != cs:
                return False
        return True
                
