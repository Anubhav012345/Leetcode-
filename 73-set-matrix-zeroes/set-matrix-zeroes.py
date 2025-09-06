class Solution:
    def mark_infinity(self,matrix,row,column):
        r=len(matrix)
        col=len(matrix[0])
        for i in range(r):
            if matrix[i][column]!=0:
                matrix[i][column]=float("inf")
        for j in range(col):
            if (matrix[row][j]!=0):
                matrix[row][j]=float("inf")


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        col=len(matrix[0])
        for i in range(rows):
            for j in range(col):
                if(matrix[i][j]==0):
                    self.mark_infinity(matrix,i,j)
        for i in range(rows):
            for j in range(col):
                if matrix[i][j]==float("inf"):
                    matrix[i][j]=0
        return matrix
        