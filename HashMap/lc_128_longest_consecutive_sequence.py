# 128. Longest Consecutive Sequence
# Difficulty: Medium
# 
# Problem:
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# The algorithm must run in O(n) time.
#
# Approach:
# - Use a HashSet to store all numbers for O(1) lookups.
# - A number is considered the "start" of a sequence if (num - 1) is not in the set.
# - From each sequence start, expand forward (num + 1, num + 2, ...) until the sequence breaks.
# - Track the maximum length encountered.
#
# Complexity:
# - Time: O(n) because each number is processed at most once.
# - Space: O(n) for the set.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Step 1: Edge case — empty list
        if not nums:
            return 0

        # Step 2: Insert all numbers into a set for O(1) lookups
        num_set = set(nums)
        longest = 0

        # Step 3: Iterate over the set
        for num in num_set:
            # Only start a sequence if this number has no predecessor
            if num - 1 not in num_set:
                current = num
                length = 1

                # Expand the sequence forward
                while current + 1 in num_set:
                    current += 1
                    length += 1

                # Update longest sequence found
                longest = max(longest, length)

        return longest


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(sol.longestConsecutive(nums))  # Output: 4
