class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        def backtrack(remain, combo, start):
            # Base Case: We found a valid combination
            if remain == 0:
                results.append(list(combo))
                return
            # Base Case: We exceeded the target
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                # Add the number to the current combination
                combo.append(candidates[i])
                
                # Recursively call backtrack with the updated remainder.
                # Notice we pass 'i' as the start index instead of 'i + 1' 
                # because we can reuse the same element.
                backtrack(remain - candidates[i], combo, i)
                
                # Backtrack: remove the last number added to try the next candidate
                combo.pop()

        backtrack(target, [], 0)
        return results
