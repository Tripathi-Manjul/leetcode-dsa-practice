class Solution:
    def trap(self, height: list[int]) -> int:
        # Two-pointer boundaries
        left = 0
        right = len(height) - 1

        # Track the highest bars seen so far from both sides
        leftMax = height[left]
        rightMax = height[right]

        # Accumulated trapped water
        res = 0

        # Process until the two pointers meet
        while left < right:

            # The smaller boundary determines where water can be computed
            if leftMax < rightMax:
                # Move the left pointer inward
                left += 1

                # Update the maximum height seen from the left
                leftMax = max(leftMax, height[left])

                # If the current bar is lower than the boundary,
                # water can be trapped above it
                res += (leftMax - height[left])

            else:
                # Move the right pointer inward
                right -= 1

                # Update the maximum height seen from the right
                rightMax = max(rightMax, height[right])

                # Compute water trapped on the right side
                res += (rightMax - height[right])

        return res
