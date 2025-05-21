from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        # Early exit: if s1 is longer, no permutation can fit into s2
        if s1_len > s2_len:
            return False

        # Frequency map of characters in s1
        s1_map = Counter(s1)

        # Initialize the frequency map for the first window in s2
        window_map = Counter(s2[:s1_len])

        # Check if the first window matches s1's character frequencies
        if window_map == s1_map:
            return True

        # Slide the window one character at a time across s2
        for i in range(s1_len, s2_len):
            incoming = s2[i]                     # Character entering the window
            outgoing = s2[i - s1_len]            # Character leaving the window

            window_map[incoming] += 1            # Add incoming character count
            window_map[outgoing] -= 1            # Subtract outgoing character count

            # Remove the character key if its count becomes zero
            if window_map[outgoing] == 0:
                del window_map[outgoing]

            # Compare updated window_map with s1_map
            if window_map == s1_map:
                return True

        # No permutation of s1 found in s2
        return False
