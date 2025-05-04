# LC 169 - Majority Element
# Problem: Find the element that appears more than ⌊n / 2⌋ times in the list.
# Assumption: Majority element always exists in the input array.

from collections import Counter
from typing import List

class Solution:

    # Approach 1: Using HashMap (collections.Counter)
    # TC = O(n) ; SC = O(n)	
    def majorityElement_counter(self, nums: List[int]) -> int:
        """
        Uses a hash map to count frequencies of elements.
        Time: O(n)
        Space: O(n)
        """
        nums_map = Counter(nums)  # Count frequency of each element
        for key, value in nums_map.items():
            # Check if any element occurs more than ⌊n / 2⌋ times
            if value > len(nums) // 2:
                return key


    # Approach 2: Boyer-Moore Majority Vote Algorithm ✅ highly preferred
    # TC = O(n) ; SC = O(1)
    def majorityElement_boyer_moore(self, nums: List[int]) -> int:
        """
        Uses Boyer-Moore Voting Algorithm to find the majority element.
        Time: O(n)
        Space: O(1)
        """
        count = 0
        candidate = None

        for num in nums:
            # When count drops to zero, set new candidate
            if count == 0:
                candidate = num

            # Increment if same as candidate, else decrement
            count += (1 if num == candidate else -1)

        return candidate


# Example usage
if __name__ == "__main__":
    nums = [3, 2, 3]
    sol = Solution()

    print("Using Counter approach:", sol.majorityElement_counter(nums))       # Output: 3
    print("Using Boyer-Moore approach:", sol.majorityElement_boyer_moore(nums))  # Output: 3
