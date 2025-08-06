class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        LeetCode 345 - Reverse Vowels of a String

        Given a string, reverse only the vowels and return the resulting string.
        Modifications must be done in-place (by converting to a mutable list).
        """

        # Define vowel set for O(1) membership check (both uppercase and lowercase)
        vowels = set('aeiouAEIOU')

        # Convert the string to a list since Python strings are immutable
        s = list(s)

        # Initialize two pointers
        left, right = 0, len(s) - 1

        # Iterate while pointers have not crossed
        while left < right:
            # Move left pointer forward if not pointing to a vowel
            if s[left] not in vowels:
                left += 1
            # Move right pointer backward if not pointing to a vowel
            elif s[right] not in vowels:
                right -= 1
            else:
                # Both s[left] and s[right] are vowels → swap them
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # Convert list back to string before returning
        return ''.join(s)
