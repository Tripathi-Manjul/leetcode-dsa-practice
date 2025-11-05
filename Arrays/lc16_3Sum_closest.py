class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # --- Update closest_sum if this is nearer to target ---
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # --- Adjust pointers based on sum comparison ---
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Perfect match; cannot get closer
                    return current_sum

        return closest_sum
