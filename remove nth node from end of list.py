class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the head
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # Move both pointers until fast reaches the last node
        # slow will end up at the node right BEFORE the one to be deleted
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # Skip the nth node
        slow.next = slow.next.next
        
        return dummy.next