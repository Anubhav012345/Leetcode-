# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        lst=[]
        while temp is not None:
            lst.append(temp.val)
            temp=temp.next
        lst.sort()
        index=0
        temp=head
        while temp is not None:
            temp.val=lst[index]
            temp=temp.next
            index+=1
        return head

