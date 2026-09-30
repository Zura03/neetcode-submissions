class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Add a dummy node to handle edge cases
        slow, fast = dummy, dummy
        
        # Move fast pointer `n+1` steps ahead to create a gap of `n` between slow and fast
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next
