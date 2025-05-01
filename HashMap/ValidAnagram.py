# Time Complexity: O(n)
# Space Complexity: O(1) — max 26 lowercase characters

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        t_map = Counter(t)

        if s_map == t_map :
            return True

        return False
