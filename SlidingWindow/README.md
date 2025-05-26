# Sliding Window Pattern – LeetCode Practice Notes

This directory contains curated problems and reference notes for the **Sliding Window** pattern, widely used in string, array, and substring/window-based problems.

---

## 🔍 When to Use Sliding Window

Use the sliding window pattern when:
- The problem involves **contiguous subarrays/substrings**.
- You are asked to find the **maximum/minimum/target condition** in a subarray.
- The input is a **linear structure** (string, array).
- Brute force uses nested loops; you want to optimize to O(n).


## 📚 What is Sliding Window?

A technique to reduce nested loops in problems involving substrings, subarrays, or contiguous sequences by maintaining a "window" over the input and moving it efficiently.

### Types of Sliding Window:

| Type | Description | Common Use |
|------|-------------|-------------|
| Fixed-length | Window size is constant | Permutation checks, substring frequency |
| Variable-length | Window expands/contracts dynamically | Longest substring without repetition, minimal window substring |

---

## window size calculation 
`right - left + 1` 
- This represents the current size of the window from `left` to `right` (inclusive).

## 🧠 Sliding Window Template

```python
def sliding_window(s):
    left = 0
    window_data = set()  # or dict for frequency
    max_result = 0
    
    for right in range(len(s)):
        # Handle duplicates/constraint violation
        while s[right] in window_data:
            window_data.remove(s[left])
            left += 1
        
        window_data.add(s[right])
        max_result = max(max_result, right - left + 1)
    
    return max_result
```

## 🧠 General Template

### Fixed-Length Window (with frequency array/map):

```python
# Initialize frequency maps
for c in pattern:
    target_count[c] += 1

# Initialize the window
for c in s[:len(pattern)]:
    window_count[c] += 1

# Slide the window
for i in range(len(pattern), len(s)):
    window_count[s[i - len(pattern)]] -= 1
    window_count[s[i]] += 1
    if window_count == target_count:
        result.append(i - len(pattern) + 1)
```

### Variable-Length Window:
```python
def variable_window(s):
    from collections import defaultdict

    left = 0
    window_count = defaultdict(int)

    for right in range(len(s)):
        window_count[s[right]] += 1

        # Shrink window if invalid
        while <invalid_window_condition>:
            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            left += 1

        # Process valid window (e.g., update max length, store indices)
```

