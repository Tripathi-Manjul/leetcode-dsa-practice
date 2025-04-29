class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        m = len(p)

        # If pattern is longer than source string, return empty list
        if n < m:
            return []

        # Helper function to map character to index (0–25)
        def idx(c):
            return ord(c) - ord('a')

        # Frequency count arrays for target string and current window
        targetCount = [0] * 26
        windowCount = [0] * 26

        # Initialize frequency count for pattern string
        for char in p:
            targetCount[idx(char)] += 1

        # Initialize frequency count for first window in 's'
        for ch in s[:m]:
            windowCount[idx(ch)] += 1

        result = []

        # Check first window match
        if windowCount == targetCount:
            result.append(0)

        # Slide the window across 's'
        for i in range(m, n):
            # Remove the character going out of window
            windowCount[idx(s[i - m])] -= 1
            # Add the character coming into the window
            windowCount[idx(s[i])] += 1

            # Compare frequency arrays
            if windowCount == targetCount:
                result.append(i - m + 1)

        return result

# Example usage (for testing)
# s = "aaaaaaaaaa" 
# p = "aaaaaaaaaaaaa"
# sol = Solution()
# print(sol.findAnagrams(s, p))  # Output: []
