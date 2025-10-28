# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # maxi=float("-inf")
    # def solve(self,root):
    #     if not root:
    #         return 0
    #     leftsum=self.solve(root.left)
    #     if leftsum<0:
    #         return 0
    #     rightsum=self.solve(root.right)
    #     if rightsum<0:
    #         return 0
    #     self.maxi=max(self.maxi,leftsum+root.val+rightsum)
    #     return root.val+max(leftsum,rightsum)


    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     self.solve(root)
    #     # if(self.maxi==0):
    #     #     return root.val
    #     return self.maxi

      maxi = float("-inf")
      def findMaxPathSum(self, root):
        if not root:
            return 0
        leftPathSum = self.findMaxPathSum(root.left)
        rightPathSum = self.findMaxPathSum(root.right)
        if leftPathSum < 0:
            leftPathSum = 0
        if rightPathSum < 0:
            rightPathSum = 0
        self.maxi = max(self.maxi, leftPathSum + root.val + rightPathSum)
        return max(leftPathSum, rightPathSum) + root.val
      def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findMaxPathSum(root)
        return self.maxi
        