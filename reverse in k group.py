class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        # Dummy node to handle the new head easily
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        nxt = dummy
        prev = dummy
        
        # Count total nodes to determine how many groups to reverse
        count = 0
        while curr.next:
            curr = curr.next
            count += 1
            
        while count >= k:
            curr = prev.next # The start of the current group
            nxt = curr.next  # The node following the current start
            # Standard in-place reversal for k-1 connections
            for _ in range(1, k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            prev = curr # Move prev to the end of the reversed group
            count -= k
            
        return dummy.next
