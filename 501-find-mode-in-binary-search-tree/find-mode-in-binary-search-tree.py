# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,node):
        lst=[]
        if node==None:
            return []
        lst=[node.val]
        lst+=self.preorder(node.left)
        lst+=self.preorder(node.right)
        return lst

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans=self.preorder(root)
        hash_map={}

        for i in range(len(ans)):
            hash_map[ans[i]]=hash_map.get(ans[i],0)+1

        maxi=float("-inf")

        for key,value in hash_map.items():
            maxi=max(maxi,value)

        lst=[]
        for key,value in hash_map.items():
            if maxi==value:
                lst.append(key)
        return lst


        