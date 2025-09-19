# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        while temp is not None:
            length+=1
            temp=temp.next
        if(length==n):
            new_head=head.next
            del head
            return new_head
        position_to_step=length-n
        temp=head
        count=1
        while position_to_step>count:
            temp=temp.next
            count+=1
        temp.next=temp.next.next
        return head


        