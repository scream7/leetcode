class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(0,2**len(nums)):
            loop = bin(i)[2:]
            if len(loop) < len(nums):
                addup = "0" * (len(nums) - len(loop))
                loop = addup + loop
            row = []
            for i,c in enumerate(loop):
                if c == '1':
                    row.append(nums[i])
            res.append(row)
        return res
