from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if either string is empty, no valid window exists
        if not s or not t:
            return ""

        # Frequency map for characters in t (our target)
        target_count = Counter(t)  # e.g., t = "ABC" => {'A':1, 'B':1, 'C':1}

        # Current frequency of characters in the sliding window
        window_count = defaultdict(int)

        have = 0                            # Number of characters that meet required frequency
        need = len(target_count)           # Total unique characters required from t

        res = (float('inf'), 0, 0)         # Track the best (smallest) window: (length, left, right)
        left = 0                           # Left pointer of the sliding window

        # Expand the right pointer of the window
        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1        # Add current character to the window

            # Check if current character meets the required frequency
            if char in target_count and window_count[char] == target_count[char]:
                have += 1

            # If all required characters are present in current window
            while have == need:
                # Update the result if the current window is smaller
                if (right - left + 1) < res[0]:
                    res = (right - left + 1, left, right)

                # Start to contract the window from the left
                left_char = s[left]
                window_count[left_char] -= 1  # Remove char at left from window

                # If removed char was a required one and its count fell below target
                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    have -= 1  # Window is no longer valid

                left += 1  # Move the left pointer forward to shrink the window

        # Extract the window substring using recorded indices
        window_len, start, end = res
        return s[start:end+1] if window_len != float('inf') else ""
