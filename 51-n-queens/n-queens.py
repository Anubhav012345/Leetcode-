class Solution:
    def solve(self,col,board,leftrow,lowerdiagonal,upperdiagonal,ans,n):
        if col==n:
            ans.append(board.copy())
            return
        for row in range(n):
            low_diagonal=row+col
            up_diagonal=n-1+col-row
            if(leftrow[row]==0 and lowerdiagonal[low_diagonal]==0 and upperdiagonal[up_diagonal]==0):
                board[row]=board[row][:col]+ "Q" +board[row][col+1:]
                leftrow[row]=1
                lowerdiagonal[low_diagonal]=1
                upperdiagonal[up_diagonal]=1
                self.solve(col+1,board,leftrow,lowerdiagonal,upperdiagonal,ans,n)
                board[row]=board[row][:col]+"."+board[row][col+1:]
                leftrow[row]=0
                lowerdiagonal[low_diagonal]=0
                upperdiagonal[up_diagonal]=0                      
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=["."*n for _ in range(n)]
        leftrow=[0]*n
        lowerdiagonal=[0]*(2*n-1)
        upperdiagonal=[0]*(2*n-1)
        self.solve(0,board,leftrow,lowerdiagonal,upperdiagonal,ans,n)
        return ans
        