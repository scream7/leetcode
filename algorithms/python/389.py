class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ms = {}
        mt = {}
        for cs in s:
            if cs not in ms.keys():
                ms[cs] = 0
            else:
                ms[cs] += 1
        for ct in t:
            if ct not in mt.keys():
                mt[ct] = 0
            else:
                mt[ct] += 1
        
        for key in mt.keys():
            if key not in ms.keys() or ms[key] != mt[key]:
                return key
