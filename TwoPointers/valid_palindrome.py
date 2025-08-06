class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Normalize the input string
        # - Convert to lowercase
        # - Filter only alphanumeric characters
        cleaned_input = ''.join(
            char.lower() for char in s if char.isalnum()
        )

        # Step 2: Initialize two pointers at the start and end of the cleaned string
        left, right = 0, len(cleaned_input) - 1

        # Step 3: Compare characters from both ends moving toward the center
        while left < right:
            if cleaned_input[left] != cleaned_input[right]:
                # If mismatch is found, it is not a palindrome
                return False
            left += 1
            right -= 1

        # Step 4: If all characters matched, it is a palindrome
        return True


