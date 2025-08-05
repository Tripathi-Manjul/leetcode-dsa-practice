class Solution:
    def is_palindrome_range(self, s: str, left: int, right: int) -> bool:
        """
        Helper function to check if s[left:right+1] is a palindrome.
        This assumes no more deletions are allowed.
        """
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        """
        Main function to check if the input string can be a palindrome
        after deleting at most one character.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Skip either the left or the right character, and check if the rest is a palindrome
                return (
                    self.is_palindrome_range(s, left + 1, right) or
                    self.is_palindrome_range(s, left, right - 1)
                )
            left += 1
            right -= 1

        # No mismatch found; already a palindrome
        return True
