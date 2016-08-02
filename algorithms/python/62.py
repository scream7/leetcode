class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*n for _ in range(m)]
        for _m in range(1,m):
            for _n in range(1,n):
                dp[_m][_n] = dp[_m-1][_n] + dp[_m][_n-1]
        return dp[-1][-1]
