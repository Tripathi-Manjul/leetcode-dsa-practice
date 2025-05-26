class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Edge case: if k is zero or exceeds array size, return None
        if k == 0 or k > len(nums):
            return None

        # Initialize window pointers and tracking variables
        left = 0
        zero_count = 0
        max_len = 0

        # Iterate using the right pointer to expand the sliding window
        for right in range(len(nums)):
            # If current element is zero, increment zero count in the window
            if nums[right] == 0:
                zero_count += 1

            # If window becomes invalid (more than k zeros), shrink from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # Shrink the window

            # Update the maximum valid window length seen so far
            max_len = max(max_len, right - left + 1)

        return max_len


# Example usage
sol = Solution()
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(sol.longestOnes(nums, k))  # Output: 10
