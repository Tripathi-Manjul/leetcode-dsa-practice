class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # --- Skip duplicate 'first' elements (base of triplet) ---
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # --- Skip duplicates for 'second' and 'third' elements ---
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result


# ============================================================
# Step 6: Example Walkthrough for Uniqueness Guarantee
# ============================================================
# Input:
# nums = [-2, -2, 0, 0, 2, 2]
# After sorting: nums = [-2, -2, 0, 0, 2, 2]
#
# --- Trace of Algorithm ---
#
# Iteration 1: i = 0, nums[i] = -2
#   target = 2
#   left = 1 (nums[left] = -2), right = 5 (nums[right] = 2)
#     current_sum = -2 + 2 = 0 < 2 → left++
#   left = 2 (nums[left] = 0), right = 5 (nums[right] = 2)
#     current_sum = 0 + 2 = 2 == target
#     -> triplet found: [-2, 0, 2]
#     -> move left++, right-- (left = 3, right = 4)
#     -> skip duplicates:
#        nums[left] == nums[left - 1] (0 == 0) → left++
#        nums[right] == nums[right + 1] (2 == 2) → right--
#     -> left = 4, right = 3 → exit while loop
#
# Iteration 2: i = 1, nums[i] = -2
#   nums[i] == nums[i-1] → duplicate base → skip
#
# Iteration 3: i = 2, nums[i] = 0
#   target = 0
#   left = 3 (nums[left] = 0), right = 5 (nums[right] = 2)
#     current_sum = 0 + 2 = 2 > 0 → right--
#   left = 3, right = 4
#     current_sum = 0 + 2 = 2 > 0 → right--
#   left = 3, right = 3 → exit while loop
#
# Iteration 4: i = 3, nums[i] = 0
#   nums[i] == nums[i-1] → duplicate base → skip
#
# --- Final Result ---
# result = [[-2, 0, 2]]
#
# --- Why Uniqueness Is Guaranteed ---
# 1. Sorted array groups duplicates together.
# 2. 'i' duplicate check → unique first element only once.
# 3. 'left'/'right' duplicate checks → skip contiguous same-value pairs.
# 4. Pointers move monotonically → no pair revisited.
# 5. Combined → every (a, b, c) unique triplet appears exactly once.
# ============================================================


# Example test
nums = [-2, -2, 0, 0, 2, 2]
print(Solution().threeSum(nums))  # Expected Output: [[-2, 0, 2]]
