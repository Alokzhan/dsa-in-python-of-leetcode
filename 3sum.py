class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Step 1: Sort the array to handle duplicates and use two pointers
        nums.sort()
        
        for i, a in enumerate(nums):
            # If the current value is the same as the previous, skip it to avoid duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Use two pointers to find two other numbers that sum to -a
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # Move left pointer and skip duplicates for the second element
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
