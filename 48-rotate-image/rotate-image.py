# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         r=len(matrix)
#         c=len(matrix[0])
#         result=[[0]*r for _ in range (c)]
#         for i in range(r):
#             for j in range(i,r):
#                 result[j][(r-1)-i]=matrix[i][j]
#         return result
        


# from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
