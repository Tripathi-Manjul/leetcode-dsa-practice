# HashMap Pattern – LeetCode Practice Notes

This directory tracks problems based on hash-based lookups, frequency counting, and map-based logic — common in string, array, and counting problems.

---

## 🔁 Core Use Cases of HashMaps in LeetCode

| Use Case | Examples | Pattern |
|----------|----------|---------|
| Frequency counting | Ransom Note (LC #383), Valid Anagram (LC #242) | `dict` / `Counter` |
| Complement lookup | Two Sum (LC #1) | Store seen values with index |
| Deduplication / Set match | Intersection of Arrays (LC #349) | Use set/hashmap to filter |
| Frequency → Heap crossover | Top K Frequent Elements (LC #347) | Map + Heap combo |
| Majority vote logic (O(1) space) | Majority Element (LC #169)                     | Boyer-Moore Voting Algorithm     |
---

# Generalized Frequency Count Template (Manual `dict`)

```python
freq_map = {}

for char in s:
    freq_map[char] = freq_map.get(char, 0) + 1
```

# Generalized Frequency Count Template (Using Counter)
from collections import Counter

freq_map = Counter(s)

# Boyer-Moore Voting Algorithm – Explanation and Use Case
⏱ Time and Space Complexity

    Time Complexity: O(n) – single traversal

    Space Complexity: O(1) – no additional data structures used

The Boyer-Moore Voting Algorithm is a space-optimized technique for finding the majority element, i.e., the element that appears more than ⌊n / 2⌋ times in an array.
✅ When to Use

    You are guaranteed that a majority element exists

    You want to avoid hash maps and use O(1) space

    You want O(n) time complexity

🔁 Step-by-step Logic

    Initialize count = 0 and candidate = None

    For each element num in the array:

        If count == 0, set candidate = num

        If num == candidate, increment count

        Else, decrement count

    Return candidate — guaranteed to be the majority

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```
