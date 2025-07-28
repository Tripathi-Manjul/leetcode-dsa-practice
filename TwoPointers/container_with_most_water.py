# lc11_container_with_most_water.py
# Leetcode 11 – Container With Most Water
# Category: Two Pointers
# Difficulty: Medium

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds the maximum water a container can store, using two-pointer approach.

        Args:
        height (List[int]): Heights of vertical lines on the x-axis.

        Returns:
        int: Maximum water that can be stored.

        Approach:
        - Initialize two pointers at the start and end of the array.
        - Calculate area formed by lines at these pointers.
        - Move the pointer pointing to the shorter line inward.
        - Repeat until pointers meet.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_area = max(max_area, width * min_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
