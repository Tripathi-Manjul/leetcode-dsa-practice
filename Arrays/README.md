# Two-Pointer Problem Patterns

This README explains the differences between the **Container With Most Water** and **Trapping Rain Water** problems, outlines their solution approaches, and provides guidance for maintaining your repository.

## File Naming

- **Filename:** `README.md`  
- **Location:** Place this file at the root of the `TwoPointers/` directory (or your main project root) so it is immediately visible.

## 1. Problem Summaries

### 1.1 Container With Most Water
- **Goal:** Find two lines that, together with the x-axis, form a container holding the maximum amount of water.  
- **Output:** A single integer representing the maximum area.

### 1.2 Trapping Rain Water
- **Goal:** Given an elevation map, calculate how much water it can trap after raining.  
- **Output:** Total units of water trapped across all bars.

## 2. Approach Comparison

| Aspect               | Container With Most Water                                                                 | Trapping Rain Water                                                          |
|----------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Objective**        | Maximize one container area                                                               | Sum water at every bar                                                        |
| **Pointer Movement** | Move the shorter line’s pointer inward to seek a taller boundary that may increase area.  | Move the pointer at the lower bar inward; for each bar, accumulate `running_max - height[i]` if below running max. |
| **State Tracked**    | Single variable `max_area`                                                                | Two running maxima (`left_max`, `right_max`) plus accumulator `water`         |
| **Time Complexity**  | O(n)                                                                                      | O(n)                                                                          |
| **Space Complexity** | O(1)                                                                                      | O(1)                                                                          |

## 3. Solution Overviews

### 3.1 Container With Most Water
```python
def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        h = min(height[left], height[right])
        area = h * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

def trap(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
