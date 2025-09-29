class Solution:
    def safe(self,row,col,board,n):
        duprow=row
        dupcol=col
        while row>=0 and col>=0:
            if board[row][col]=="Q":
                return False
            row-=1
            col-=1
        row=duprow
        col=dupcol
        while col>=0:
            if board[row][col]=="Q":
                return False
            col-=1
        row=duprow
        col=dupcol
        while row<n and col>=0:
            if board[row][col]=="Q":
                return False
            col-=1
            row+=1
        return True
    
    def solve(self,col,board,ans,n):
        if col==n:
            ans.append(board.copy())
            return
        for j in range(n):
            if self.safe(j,col,board,n):
                board[j]=board[j][:col]+"Q"+board[j][col+1:]
                self.solve(col+1,board,ans,n)
                board[j]=board[j][:col]+"."+board[j][col+1:]                

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=["."*n for _ in range(n)]
        self.solve(0,board,ans,n)
        return ans
        