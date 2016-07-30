class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        res.append([1])
        res.append([1,1])
        if numRows <=2 :
            return res[:numRows]
        else:
            for i in range(2,numRows):
                row = [1 for _ in range(i+1)]
                upRow = res[i-1]
                for j in range(1,i):
                    row[j] = upRow[j-1] + upRow[j]
                res.append(row)
        return res
