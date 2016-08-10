class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            dic = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif dic.get(board[i][j]) != None:
                    return False
                else:
                    dic[board[i][j]] = True
                    
        for i in range(9):
            dic = {}
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif dic.get(board[j][i]) != None:
                    return False
                else:
                    dic[board[j][i]] = True
                    
                
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                dic = {}
                for k in square:
                    if k == '.':
                        continue
                    elif dic.get(k) != None:
                        return False
                    else:
                        dic[k] = True

        return True
