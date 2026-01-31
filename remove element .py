class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k will be the index for the next non-val element
        k = 0
        
        for i in range(len(nums)):
            # If the current element is NOT the value we want to remove
            if nums[i] != val:
                # Move it to the position k and increment k
                nums[k] = nums[i]
                k += 1
                
        return k
