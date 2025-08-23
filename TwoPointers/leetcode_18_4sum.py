from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Solve the 4Sum problem:
        Find all unique quadruplets [a, b, c, d] such that:
            nums[a] + nums[b] + nums[c] + nums[d] == target
        
        Approach:
        - Sort the array
        - Fix two numbers using two nested loops
        - Use two-pointer technique on the remaining two numbers
        - Skip duplicates to ensure uniqueness
        
        Time Complexity: O(n^3)
        Space Complexity: O(1) (ignoring result storage)
        """

        # Step 1: Sort the array to enable two-pointer strategy and easy duplicate handling
        nums.sort()
        n = len(nums)
        results = []

        # Step 2: Outer loop for the first number
        for i in range(n - 3):
            # Skip duplicate 'i' values to avoid repeated quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Second loop for the second number
            for j in range(i + 1, n - 2):
                # Skip duplicate 'j' values (similar logic as for 'i')
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Step 4: Initialize two pointers for the remaining two numbers
                left, right = j + 1, n - 1

                # Step 5: Two-pointer scan
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        # Found a valid quadruplet
                        results.append([nums[i], nums[j], nums[left], nums[right]])

                        # Move both pointers to find next candidate
                        left += 1
                        right -= 1

                        # Skip duplicates for 'left'
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Skip duplicates for 'right'
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        # If sum is too small, increase it by moving left pointer
                        left += 1
                    else:
                        # If sum is too large, decrease it by moving right pointer
                        right -= 1

        return results
