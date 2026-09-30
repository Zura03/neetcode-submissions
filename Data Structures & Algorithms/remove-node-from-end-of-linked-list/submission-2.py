# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L = dummy = ListNode(next=head)
        R = head
        while n > 0:
            R = R.next
            n -= 1
        while R:
            L, R = L.next, R.next
        L.next = L.next.next
        return dummy.next