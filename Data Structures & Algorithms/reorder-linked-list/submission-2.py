# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # dum=head
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        newlist=slow.next
        slow.next=None
        prev=None
        curr=newlist
        while curr:
            nextnod=curr.next
            curr.next=prev
            prev=curr
            curr=nextnod
        dummy=ListNode()
        current=dummy
        bum=head
        cum=prev
        while cum:
            temp1,temp2=bum.next,cum.next
            bum.next=cum
            cum.next=temp1
            bum,cum=temp1,temp2

            
