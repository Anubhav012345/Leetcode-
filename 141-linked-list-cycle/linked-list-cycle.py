# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set=set()
        temp=head
        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp=temp.next
        return False
        