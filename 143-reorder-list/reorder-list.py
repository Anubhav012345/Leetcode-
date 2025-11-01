# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        start = head
        while start and start.next and start.next.next:
            end = start
            while end.next and end.next.next:
                end = end.next
            last = end.next
            end.next = None
            last.next = start.next
            start.next = last
            start = last.next
            
        return
