class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = {}
        for i in nums:
            if hash.get(i) is not None:
                return True
            else:
                hash[i] = 1
        return False
