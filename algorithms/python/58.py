class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for idx in range(len(s)-1,-1,-1):
            if count == 0:
                if s[idx] != ' ':
                    count += 1
            else:
                if s[idx] == ' ':
                    break
                else:
                    count += 1
        return count
