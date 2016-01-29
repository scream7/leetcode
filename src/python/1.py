class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index={}
        for i,num in enumerate(nums):
            if target - num in index:
                return [index[target - num] + 1,i+1]
            else:
                index[num] = i
