# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def dfs(node):
            c = 0
            if node.next:
                c = dfs(node.next)
            d = node.val * 2 + c
            node.val = (d % 10)
            return d // 10
            
        c = dfs(head)

        if c > 0:
            node = ListNode(c, head)
            return node

        return head