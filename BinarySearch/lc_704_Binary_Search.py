class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Perform binary search on a sorted array to find the target.

        Binary search works by repeatedly dividing the search interval in half.
        At each step:
        1. Compute the midpoint of the current interval.
        2. Compare nums[mid] with the target.
        3. Move either to the left half or the right half accordingly.

        This algorithm guarantees O(log n) time complexity.
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            # Compute midpoint safely.
            # Using (left + right) // 2 ensures an integer index.
            # The '//' operator performs floor division, meaning the result
            # is always an integer (required for valid array indexing).
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # If target lies in the left half, discard the right half
            if target < nums[mid]:
                right = mid - 1
            else:
                # Otherwise discard the left half
                left = mid + 1

        # Target does not exist in the array
        return -1


        