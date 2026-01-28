class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        col=len(matrix[0])
        result=[([0]*col)for _ in range(rows)]

        for i in range(rows):
            for j in range(col):
                if(matrix[i][j]==-1):
                    val=self.maximumelement(matrix,j)
                    matrix[i][j]=val
                result[i][j]=matrix[i][j]
        return result        

    def maximumelement(self,matrix,col):
        rows=len(matrix)
        col_max=matrix[0][col]
        for i in range(rows):
            if matrix[i][col] > col_max:
                col_max = matrix[i][col]
        return col_max