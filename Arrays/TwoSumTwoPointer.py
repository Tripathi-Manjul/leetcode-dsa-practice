from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Pair each value with its original index
        nums_pair = [(value, index) for index, value in enumerate(nums)]
        # Sort by the value
        nums_pair.sort(key=lambda x: x[0])

        left, right = 0, len(nums_pair) - 1

        # Move two pointers inward to find the target sum
        while left < right:
            current_sum = nums_pair[left][0] + nums_pair[right][0]
            if current_sum == target:
                # Return original indices
                return [nums_pair[left][1], nums_pair[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        # Problem guarantees exactly one solution; this line is unreachable
        return []

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))  # Output: [0, 1]
