class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given a string `s` consisting of uppercase English letters and an integer `k`,
        returns the length of the longest substring that can be transformed into
        a string with all identical characters after performing at most `k` replacements.
        """
        
        # Frequency map for characters within the current sliding window
        freq = {}

        # Left pointer of the sliding window
        left = 0
        
        # Tracks the count of the most frequent character in the current window.
        # This allows us to know how many replacements we need to make all characters uniform.
        max_freq = 0
        
        # Stores the result — maximum valid window length found so far.
        max_length = 0

        # Iterate through the string using the right pointer
        for right in range(len(s)):
            # Include the character at position `right` in the window
            char = s[right]
            freq[char] = freq.get(char, 0) + 1

            # Update the most frequent character count in the window
            max_freq = max(max_freq, freq[char])

            # If replacements needed exceed k → window invalid, so shrink from the left
            # replacements_needed = window_size - max_freq
            while (right - left + 1) - max_freq > k:
                left_char = s[left]
                freq[left_char] -= 1  # Remove one occurrence of the leftmost character
                left += 1             # Move left pointer to shrink the window

            # Update the result with the current valid window size
            max_length = max(max_length, right - left + 1)

        # Return the length of the longest valid window
        return max_length
