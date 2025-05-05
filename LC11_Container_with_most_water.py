class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize the variable that will hold the maximum area found
        max_area = 0
        
        # Set two pointers at the ends of the height array
        left_pointer = 0
        right_pointer = len(height) - 1

        # Continue until the pointers cross
        while left_pointer < right_pointer:
            # Compute the width between the two lines
            width = right_pointer - left_pointer
            # The container height is limited by the shorter line
            limiting_height = min(height[left_pointer], height[right_pointer])
            # Calculate the area with the current pair of lines
            current_area = limiting_height * width
            # Update the maximum area if this configuration is larger
            max_area = max(max_area, current_area)

            # Advance the pointer at the shorter line to seek a taller boundary
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area
