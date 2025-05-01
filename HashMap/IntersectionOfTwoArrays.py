# Time Complexity: O(n + m)
#  - Converting both lists to sets: O(n) + O(m)
#  - Set intersection: O(min(n, m))

# Space Complexity: O(n + m)
#  - Stores both sets in memory

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Efficient set-based solution to find unique intersection elements.

        1. Convert both input lists to sets — removes duplicates automatically.
        2. Use `&` operator to compute set intersection (i.e., common elements).
        3. Convert the result back to a list before returning.

        Example:
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        Output → [2]
        """
        return list(set(nums1) & set(nums2))
