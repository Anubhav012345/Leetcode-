class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            rows=len(mat)
            col=len(mat[0])
            for i in range(rows):
                for j in range(i+1,col):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
                
            for row in mat:
                row.reverse()
        
        for _ in range(4):
            if(mat==target):
                return True
            rotate(mat)
        return False
            
        