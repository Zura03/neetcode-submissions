class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list (slow, fast pointers)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow.next
        slow.next = None  # Terminate the first half
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
