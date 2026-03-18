class Solution:
    def totalNQueens(self, n: int) -> int:
        def NQueens(board, row):
            if row==len(board):
                return 1
                
            count=0
            for col in range(len(board)):
                if isSafe(board, row, col):
                    board[row][col] = 'Q'
                    count+=NQueens(board, row+1)
                    board[row][col] = '.'
                    
            return count

        # checking queen place position
        def isSafe(board, row, col):
            # vertical up
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # diagonal left
            maxLeft = min(row, col)
            for i in range(1,maxLeft+1):
                if board[row-i][col-i] == 'Q':
                    return False
                    
            # diagonal right
            maxRight = min(row, len(board)-col-1)
            for i in range(1,maxRight+1):
                if board[row-i][col+i] == 'Q':
                    return False

            return True

        # for nxn matrix
        def matrix(r,c,value):
            return [[value for _ in range(c)] for _ in range(r)]

        board = matrix(n,n,'.')
        return NQueens(board, 0)


                
         

       