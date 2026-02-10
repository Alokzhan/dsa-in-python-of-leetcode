class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(current_path, options):
            
            if len(current_path) == len(nums):
                res.append(current_path[:]) 
                return
            
            for i in range(len(options)):
               
                choice = options[i]
                current_path.append(choice)
                
               
                remaining = options[:i] + options[i+1:]
                backtrack(current_path, remaining)
                
               
                current_path.pop()

        backtrack([], nums)
        return res
