class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Early exit: if s1 is longer, s2 cannot contain its permutation
        if len(s1) > len(s2):
            return False

        # Fixed-size frequency arrays (26 letters for 'a' to 'z')
        s1_count = [0] * 26
        window_count = [0] * 26

        # Build frequency map for s1
        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1

        # Initialize the first window in s2
        for ch in s2[:len(s1)]:
            window_count[ord(ch) - ord('a')] += 1

        # Check the first window
        if window_count == s1_count:
            return True

        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add one character (incoming)
            window_count[ord(s2[i]) - ord('a')] += 1
            # Remove one character (outgoing)
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # Compare after sliding
            if window_count == s1_count:
                return True

        # No permutation match found
        return False
