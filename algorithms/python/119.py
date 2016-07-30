class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        res.append([1])
        res.append([1,1])
        if rowIndex <=1 :
            return res[rowIndex]
        else:
            for i in range(2,rowIndex+1):
                row = [1 for _ in range(i+1)]
                upRow = res[i-1]
                for j in range(1,i):
                    row[j] = upRow[j-1] + upRow[j]
                res.append(row)
        return res[rowIndex]
            
        
