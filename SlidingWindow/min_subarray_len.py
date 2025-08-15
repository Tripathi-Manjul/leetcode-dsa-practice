class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray 
        whose sum is >= target. Returns 0 if no such subarray exists.

        Approach:
        - Uses the sliding window technique because the array contains only positive integers.
        - Expand the right boundary to increase sum.
        - Once the sum is >= target, shrink from the left to minimize window length.

        Time Complexity: O(n)  -> Each element is added and removed at most once.
        Space Complexity: O(1) -> Constant extra space.
        """
        left = 0               # Left boundary of the sliding window
        current_sum = 0        # Current sum of the window
        min_len = float('inf') # Stores the minimal length found

        # Expand the window by moving 'right'
        for right in range(len(nums)):
            current_sum += nums[right]

            # Contract the window from the left while the sum is still valid
            while current_sum >= target:
                # Update minimal length for the current valid window
                min_len = min(min_len, right - left + 1)

                # Shrink the window from the left
                current_sum -= nums[left]
                left += 1

        # If min_len was never updated, no valid subarray was found
        return 0 if min_len == float('inf') else min_len


# Example usage for quick verification
if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    sol = Solution()
    print(sol.minSubArrayLen(target, nums))  # Expected output: 2
