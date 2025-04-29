# Sliding Window Pattern – LeetCode Practice Notes

This directory contains curated problems and reference notes for the **Sliding Window** pattern, widely used in string, array, and substring/window-based problems.

---

## 📚 What is Sliding Window?

A technique to reduce nested loops in problems involving substrings, subarrays, or contiguous sequences by maintaining a "window" over the input and moving it efficiently.

### Types of Sliding Window:

| Type | Description | Common Use |
|------|-------------|-------------|
| Fixed-length | Window size is constant | Permutation checks, substring frequency |
| Variable-length | Window expands/contracts dynamically | Longest substring without repetition, minimal window substring |

---

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

#Variable-Length Window:
left = 0
char_map = {}
for right in range(len(s)):
    # Expand window
    char_map[s[right]] += 1

    while <invalid_window_condition>:
        # Contract window
        char_map[s[left]] -= 1
        left += 1

    # Record result if valid

