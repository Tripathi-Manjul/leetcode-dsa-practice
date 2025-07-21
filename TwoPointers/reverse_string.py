# lc344_reverse_string.py
# Leetcode 344 - Reverse String
# Category: Two Pointers
# Difficulty: Easy

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the input list of characters in-place using two pointers.

        Args:
            s (List[str]): A list of single-character strings.

        Returns:
            None: The input list is modified in-place.

        Approach:
            - Use two pointers: one from the start, one from the end.
            - Swap characters at these positions.
            - Move inward until pointers meet.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(s) - 1

        # Continue swapping until the two pointers meet or cross
        while left < right:
            # Swap characters at left and right indices
            s[left], s[right] = s[right], s[left]
            
            # Move both pointers inward
            left += 1
            right -= 1
