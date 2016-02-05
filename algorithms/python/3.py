class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #position of every char
        if len(s) <2:
            return len(s)
        pos = {}
        max_length = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in pos:
                pos[s[i]] = i
            else:
                start = max(pos[s[i]] + 1,start)
                pos[s[i]] = i
            max_length = max(max_length,i-start + 1)
        return max_length