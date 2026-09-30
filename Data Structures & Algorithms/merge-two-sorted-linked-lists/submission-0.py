# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d1, d2 = list1, list2
        dummy = node = ListNode()
        while d1 and d2:
            if d1.val < d2.val:
                node.next = d1
                d1 = d1.next
            else:
                node.next = d2
                d2 = d2.next
            node = node.next
        
        while d1:
            node.next = d1
            d1 = d1.next
            node = node.next
        while d2:
            node.next = d2
            d2 = d2.next
            node = node.next
        
        return dummy.next