class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {chr(x + ord('a')):"" for x in range(26)}
        strings = str.split(' ')
        if len(strings) != len(pattern):
            return False
        for c,string in zip(pattern,strings):
            if dic.get(c) == "":
                dic[c] = string
            if dic[c] != string or dic.values().count(string) > 1:
                return False
        return True
                
