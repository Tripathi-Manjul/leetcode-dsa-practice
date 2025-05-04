from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Count the frequency of each element in both arrays
        nums1_map = Counter(nums1)
        nums2_map = Counter(nums2)

        result = []

        # Iterate through elements in nums1_map
        for num in nums1_map:
            # If the number also exists in nums2_map
            if num in nums2_map:
                # Append the number min(count in nums1, count in nums2) times to the result
                result.extend([num] * min(nums1_map[num], nums2_map[num]))

        # Return the intersection array with correct frequencies
        return result
