class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        def backtrack(remain, combo, start):
            
            if remain == 0:
                results.append(list(combo))
                return
            
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
            
                combo.append(candidates[i])
                
             
                backtrack(remain - candidates[i], combo, i)
                
               
                combo.pop()

        backtrack(target, [], 0)
        return results
