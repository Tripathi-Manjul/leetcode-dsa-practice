class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determine whether two strings s and t are isomorphic.

        Two strings are isomorphic if there exists a one-to-one character
        mapping from s to t that preserves the order of characters.
        - Each character in s must always map to the same character in t.
        - No two distinct characters in s may map to the same character in t.
        - A character may map to itself.

        Approach:
        Use two hash maps to enforce a bijection:
        1. s_to_t: maps characters from s to corresponding characters in t.
        2. t_to_s: maps characters from t back to characters in s to ensure
           no two characters in s attempt to map to the same target.

        Time complexity: O(n), where n is the length of the strings.
        Space complexity: O(1), limited by the finite character set.
        """

        # Early exit if lengths differ. Isomorphism requires equal length.
        if len(s) != len(t):
            return False

        s_to_t = {}  # Forward mapping from s to t
        t_to_s = {}  # Reverse mapping from t to s

        # Iterate over characters in both strings in parallel
        for cs, ct in zip(s, t):

            # Validate forward mapping (s -> t)
            if cs in s_to_t:
                # Existing mapping must be consistent
                if s_to_t[cs] != ct:
                    return False
            else:
                # Establish new forward mapping
                s_to_t[cs] = ct

            # Validate reverse mapping (t -> s)
            if ct in t_to_s:
                # Reverse mapping must match forward logic
                if t_to_s[ct] != cs:
                    return False
            else:
                # Establish new reverse mapping
                t_to_s[ct] = cs

        # All constraints satisfied
        return True
