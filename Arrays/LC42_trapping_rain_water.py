class Solution:
    def trap(self, height: list[int]) -> int:
        # Initialize two pointers at the ends of the elevation map
        left = 0
        right = len(height) - 1

        # Track the highest wall seen so far from each side
        left_max = 0
        right_max = 0

        # Accumulate total trapped water
        water = 0

        # Process bars until pointers meet
        while left < right:
            # If left wall is lower, it is the limiting boundary
            if height[left] < height[right]:
                # Update left_max if this bar is taller than any seen before
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Otherwise, water accumulates above this bar
                    water += left_max - height[left]
                # Move left pointer inward to find a potentially taller wall
                left += 1
            else:
                # Right wall is lower or equal, so it limits the water
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # Water accumulates above the right bar
                    water += right_max - height[right]
                # Move right pointer inward to find a potentially taller wall
                right -= 1

        # Return the total volume of trapped water
        return water
