class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Two‑pointer approach to find the two numbers in a sorted list that sum to a given target.

        Args:
            numbers (list[int]): A sorted list of integers.
            target (int): The target sum.

        Returns:
            list[int]: A list containing the 1‑based indices of the two numbers that add up to target.
        """
        # Initialize two pointers at the ends of the list
        left, right = 0, len(numbers) - 1
        
        # Move the pointers until they meet
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Found the pair; return their 1‑based indices
                return [left + 1, right + 1]
            elif current_sum < target:
                # Sum is too small: move left pointer rightward to increase sum
                left += 1
            else:
                # Sum is too large: move right pointer leftward to decrease sum
                right -= 1
        
        # If no valid pair is found, return an empty list (or raise an exception as per requirement)
        return []
