class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize stack with -1 to serve as a boundary
        stack = [-1]
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:
                # For ')', pop the last element (either matching '(' or a boundary)
                stack.pop()
                
                if not stack:
                    # If stack is empty, this ')' is unmatched; push its index as a new boundary
                    stack.append(i)
                else:
                    # Calculate current valid length using the index at the top of stack
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
