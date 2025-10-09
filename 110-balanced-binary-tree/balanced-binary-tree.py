# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,node):
        if node==None:
            return 0
        leftheight=self.solve(node.left)
        if leftheight==-1:
            return -1
        rightheight=self.solve(node.right)
        if rightheight==-1:
            return -1
        if abs(leftheight-rightheight)>1:
            return -1
        return 1+max(leftheight,rightheight)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x=self.solve(root)
        if(x==-1):
            return False
        return True
        