from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the list `nums` that sum to zero.
        """
        # Sort the array to enable two‑pointer traversal and duplicate skipping
        nums.sort()
        result: List[List[int]] = []
        n = len(nums)

        # Iterate each number as the potential first element of the triplet
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            # Use two‑pointer technique to find pairs that sum to −nums[i]
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    # Sum too small ⇒ increase left pointer
                    left += 1
                else:
                    # Sum too large ⇒ decrease right pointer
                    right -= 1

        return result
