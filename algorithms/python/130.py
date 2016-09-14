class Solution(object):
    def dfs(self,board,i,j):
        if board[i][j] != 'O':
            return
        board[i][j] = '.'
        #up
        if i-1 > 0 and board[i-1][j] == 'O':
            self.dfs(board,i-1,j)
        #down
        if i+1 < len(board)-1 and board[i+1][j] == 'O':
            self.dfs(board,i+1,j)
        #left
        if j-1 > 0 and board[i][j-1] == 'O':
            self.dfs(board,i,j-1)
        #right
        if j+1 < len(board[i])-1 and board[i][j+1] == 'O':
            self.dfs(board,i,j+1)
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(board,i,0)
        for i in range(len(board)):
            if board[i][-1] == 'O':
                self.dfs(board,i,len(board[0])-1)
        for i in range(len(board[-1])):
            if board[0][i] == 'O':
                self.dfs(board,0,i)
        for i in range(len(board[-1])):
            if board[-1][i] == 'O':
                self.dfs(board,len(board)-1,i)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'
        
        
