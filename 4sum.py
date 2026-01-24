class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two-pointer approach for the remaining two elements
                left, right = j + 1, n - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        # Skip duplicate values for the third and fourth elements
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res
