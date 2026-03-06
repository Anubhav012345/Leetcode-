class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node, path, total):
            if not node:
                return
            path.append(node.val)
            total += node.val

            if not node.left and not node.right and total == targetSum:
                result.append(path.copy())
            
            dfs(node.left, path, total)
            dfs(node.right, path, total)

            path.pop()  
        dfs(root, [], 0)
        return result