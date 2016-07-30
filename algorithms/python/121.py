class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowestPrice = 1000000
        maxProfit = 0
        for p in prices:
            if p < lowestPrice:
                lowestPrice = p
            maxProfit = p - lowestPrice if p-lowestPrice > maxProfit else maxProfit
        return maxProfit
