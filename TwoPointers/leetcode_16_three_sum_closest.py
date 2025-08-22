class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Sort the array to enable the two-pointer technique
        nums.sort()
        n = len(nums)

        # Initialize the closest sum as infinity for comparison
        closest_sum = float('inf')

        # Iterate through each element, fixing one number at a time
        for i in range(n):
            # Skip duplicate elements to avoid redundant work
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers: one starts right after i, the other from the end
            lo, hi = i + 1, n - 1

            # Move pointers inward to explore possible triplets
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]

                # Update closest_sum if this triplet is closer to target
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                # If exact match found, return immediately
                if curr_sum == target:
                    return curr_sum
                # If sum is too small, increase it by moving lo forward
                elif curr_sum < target:
                    lo += 1
                # If sum is too large, decrease it by moving hi backward
                else:
                    hi -= 1

        # Return the closest sum after exploring all triplets
        return closest_sum
