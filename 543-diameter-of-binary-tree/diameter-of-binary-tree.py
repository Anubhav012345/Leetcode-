# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter=0
    def solve(self,node):
        if node==None:
            return 0
        leftHeight=self.solve(node.left)
        rightHeight=self.solve(node.right)
        self.diameter=max(self.diameter,leftHeight+rightHeight)
        return 1+max(leftHeight,rightHeight)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.solve(root)
        return self.diameter
        