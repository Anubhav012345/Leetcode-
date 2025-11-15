# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,target,current_sum):
        if root is None:
            return False
        current_sum=current_sum+root.val
        if root.left is None and root.right is None:
            if current_sum==target:
                return True
            else:
                return False
        left=self.solve(root.left,target,current_sum)
        if left==True:
            return True
        right=self.solve(root.right,target,current_sum)
        if right==True:
            return True
        return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        current_sum=0
        return self.solve(root,targetSum,current_sum)