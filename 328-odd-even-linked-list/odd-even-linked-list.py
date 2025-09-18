# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp=head
        lst=[]
        while temp is not None:
            lst.append(temp.val)
            if temp.next is  None:
                break
            temp=temp.next.next
        temp=head.next
        while temp is not None:
            lst.append(temp.val)
            if temp.next is None:
                break
            temp=temp.next.next
        index=0
        temp=head
        while temp is not None:
            temp.val=lst[index]
            index+=1
            temp=temp.next
        return head
        
        