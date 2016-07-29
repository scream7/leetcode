class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 :return 1
        elif n==1 or n==2: return n
        steps = [0 for _ in range(n)]
        steps[0] = 1
        steps[1] = 2
        for i in range(2,n):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[-1]
        
