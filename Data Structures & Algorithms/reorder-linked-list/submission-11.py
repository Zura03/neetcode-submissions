# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        curr=slow.next
        slow.next=None
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode #prev - first element of reversed list
        
        first,second=head,prev
        # second=prev
        while second:
            temp1,temp2=first.next,second.next
            # temp2=second.next
            first.next=second
            second.next=temp1
            first,second=temp1,temp2
            # second=temp2


