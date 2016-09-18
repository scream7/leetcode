class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #path = []
        res = []
        candidates.sort()
        self.solve(candidates,0,target,[],res)
        return res
    def solve(self,candidates,idx,target,path,res):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(idx,len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                return
            #path.append(candidates[i])
            self.solve(candidates,i+1,target-candidates[i],path + [candidates[i]],res)
            #path.pop()
        
        
