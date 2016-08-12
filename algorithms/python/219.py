class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for idx,num in enumerate(nums):
            if dic.get(num) is None:
                dic[num] = [idx]
            else:
                dic[num].append(idx)
            
        for key in dic.keys():
            for idx in range(len(dic[key]) - 1):
                if dic[key][idx+1] - dic[key][idx] <= k:
                    return True
        
        return False
