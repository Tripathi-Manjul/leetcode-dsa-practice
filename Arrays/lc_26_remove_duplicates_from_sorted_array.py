class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Edge case: if array is empty, no elements to process
        if not nums:
            return 0
        
        # 'i' is the slow pointer — it marks the position
        # where the next unique element should be placed.
        i = 0
        
        # 'j' is the fast pointer — it scans through the array
        # starting from index 1, since the first element is always unique.
        for j in range(1, len(nums)):
            
            # When a new unique element is found
            if nums[j] != nums[i]:
                # Move the slow pointer forward
                i += 1
                
                # Overwrite the next position with the new unique element
                nums[i] = nums[j]
        
        # The first (i + 1) elements are now unique
        # Return the count of unique elements
        return i + 1
