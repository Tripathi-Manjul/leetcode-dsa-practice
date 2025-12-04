class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Perform binary search on a sorted array to find the position of 'target'.

        If 'target' is found, return its index.
        If not found, return the index where it should be inserted to keep the array sorted.

        Key insight:
        After binary search finishes (when left > right), the 'left' pointer
        always ends up at the correct insertion position:
        - If target is smaller than all elements, left becomes 0.
        - If target belongs somewhere in the middle, left lands at the first
          index where nums[left] >= target.
        - If target is greater than all elements, left becomes len(nums).

        This gives an O(log n) runtime as required.
        """

        left = 0
        right = len(nums) - 1

        # Standard binary search loop
        while left <= right:
            # Floor division // ensures integer midpoint
            mid = (left + right) // 2

            if nums[mid] == target:
                # Exact match found
                return mid

            elif target < nums[mid]:
                # Target must lie in the left half
                right = mid - 1

            else:
                # Target must lie in the right half
                left = mid + 1

        # If not found: 'left' is exactly the correct insertion position.
        # (Never adjust it with +1; binary search invariants guarantee correctness.)
        return left
