class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to store frequency of characters in the current window
        count = {}
        res = 0  # Tracks the length of the longest valid substring
        l = 0    # Left pointer of the sliding window

        for r in range(len(s)):
            # Increment the count for the current character at the right pointer
            count[s[r]] = count.get(s[r], 0) + 1

            # If the number of characters to be replaced exceeds k, shrink the window
            # (window size) - (frequency of the most common character) > k
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1  # Decrement the count of the leftmost character
                l += 1            # Move the left pointer to the right

            # Update the maximum valid window size found so far
            res = max(res, r - l + 1)
        
        return res  # Return the length of the longest valid substring