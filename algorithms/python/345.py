class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = set('aeiouAEIOU')
        res = list(s)
        i, j = 0,len(s)-1
        while i < j:
            if s[i] not in dic:
                i += 1
                continue
            if s[j] not in dic:
                j -= 1
                continue
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return ''.join(res)
            
        
