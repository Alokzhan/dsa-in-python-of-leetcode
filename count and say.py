class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Start with the first term
        current_str = "1"
        
        # Generate terms from 2 up to n
        for _ in range(n - 1):
            next_str = []
            i = 0
            
            while i < len(current_str):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current_str) and current_str[i] == current_str[i+1]:
                    count += 1
                    i += 1
                
                # Append the count and the digit
                next_str.append(str(count))
                next_str.append(current_str[i])
                i += 1
            
            # Update current_str for the next iteration
            current_str = "".join(next_str)
            
        return current_str
