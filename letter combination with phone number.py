class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        # Mapping of digits to letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            # If the path length equals digits length, we found a combination
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            # Get the letters corresponding to the current digit
            possible_letters = phone_map[digits[index]]
            
            for letter in possible_letters:
                path.append(letter)           # Add letter to current path
                backtrack(index + 1, path)    # Move to the next digit
                path.pop()                    # Backtrack (remove letter)

        backtrack(0, [])
        return res
