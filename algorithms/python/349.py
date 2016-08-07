class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        idx1 = idx2 = 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
            else:
                if nums1[idx1] not in res:
                    res.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
        return res
