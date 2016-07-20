class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        ans = -10000000
        for i in range(len(nums)):
            sum += nums[i]
            if sum > ans:
                ans = sum
            if sum < 0:
                sum = 0
        return ans
