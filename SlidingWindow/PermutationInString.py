class Solution:
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


# Example usage
s1 = "ab" 
s2 = "eidbaooo"
sol = Solution()
print(sol.checkInclusion(s1, s2))  # Output: 3
