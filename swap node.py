

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        first = head
        second = head.next
        
        # Recursively swap the rest and link to current pair
        first.next = self.swapPairs(second.next)
        second.next = first
        
        # New head of this swapped pair is the 'second' node
        return second
