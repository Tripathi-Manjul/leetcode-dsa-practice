from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Given a list of fruit types (represented as integers), returns the length of the
        longest contiguous subarray that contains at most two distinct types of fruits.
        
        This simulates collecting fruits into two baskets with no limit on quantity,
        but only allowing two distinct types at a time (sliding window constraint).
        """
        max_len = 0  # Tracks the maximum number of fruits collected in any valid window
        curr_window = defaultdict(int)  # Stores the count of each fruit type in the current window
        left = 0  # Left boundary of the sliding window

        for right in range(len(fruits)):
            curr_window[fruits[right]] += 1  # Include the current fruit in the window

            # If more than 2 distinct fruit types, shrink the window from the left
            while len(curr_window) > 2:
                curr_window[fruits[left]] -= 1
                if curr_window[fruits[left]] == 0:
                    del curr_window[fruits[left]]  # Remove fruit type if count drops to 0
                left += 1  # Move left boundary to maintain at most 2 types

            # Update max_len if current window is larger
            max_len = max(max_len, right - left + 1)

        return max_len


        