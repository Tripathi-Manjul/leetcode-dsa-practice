from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Total number of elements in the array
        n = len(nums)

        # Initialize the minimum length to infinity (a value larger than any possible valid subarray length)
        min_length = float('inf')

        # This will store the current sum of the sliding window
        current_sum = 0

        # Left boundary of the sliding window
        start = 0

        # Iterate over the array using 'end' as the right boundary of the sliding window
        for end in range(n):
            # Expand the window to the right by adding the current element to the window sum
            current_sum += nums[end]

            # Try to shrink the window from the left as long as the current sum is greater than or equal to target
            while current_sum >= target:
                # Update the minimum length of the valid window
                min_length = min(min_length, end - start + 1)

                # Shrink the window from the left
                current_sum -= nums[start]
                start += 1

        # If min_length was never updated, return 0 (no valid subarray found); otherwise, return the minimum length
        return 0 if min_length == float('inf') else min_length
