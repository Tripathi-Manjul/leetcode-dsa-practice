from collections import Counter

class SolutionArray:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Return True if any permutation of s1 is a substring of s2.
        Uses a fixed‐size sliding window with character count comparison.
        """
        len_s1, len_s2 = len(s1), len(s2)
        # If s1 is longer than s2, no permutation can fit
        if len_s1 > len_s2:
            return False

        # Helper to convert character to index 0..25
        def idx(c: str) -> int:
            return ord(c) - ord('a')
        
        # Build frequency array for s1
        target = [0] * 26
        for ch in s1:
            target[idx(ch)] += 1
        
        # Initialize window frequency for the first len_s1 characters of s2
        window = [0] * 26
        for i in range(len_s1):
            window[idx(s2[i])] += 1
        
        # If initial window matches target, a permutation exists
        if window == target:
            return True
        
        # Slide the window across s2
        for i in range(len_s1, len_s2):
            # Remove character leaving the window
            outgoing = s2[i - len_s1]
            window[idx(outgoing)] -= 1
            
            # Add new character entering the window
            incoming = s2[i]
            window[idx(incoming)] += 1
            
            # Compare counts
            if window == target:
                return True
        
        # No matching window found
        return False
    

class SolutionCounter:
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




# Example usage
if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print("Array-based:", SolutionArray().checkInclusion(s1, s2))
    print("Counter-based:", SolutionCounter().checkInclusion(s1, s2))
