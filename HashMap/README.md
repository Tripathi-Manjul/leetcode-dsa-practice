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

---

##Generalized Frequency Count Template (Manual `dict`)

```python
freq_map = {}

for char in s:
    freq_map[char] = freq_map.get(char, 0) + 1


##Generalized Frequency Count Template (Using Counter)
from collections import Counter

freq_map = Counter(s)

