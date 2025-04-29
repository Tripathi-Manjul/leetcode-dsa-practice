class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store unique characters in the current window
        char_set = set()
        
        # Left pointer of the sliding window
        left = 0
        
        # Variable to track the length of the longest substring found
        max_length = 0
        
        # Iterate with the right pointer over the string
        for right in range(len(s)):
            
            # If current character is already in the set,
            # move the left pointer to remove characters until the duplicate is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set (window)
            char_set.add(s[right])
            
            # Update the max length if current window is larger
            max_length = max(max_length, right - left + 1)
        
        # Return the length of the longest valid substring
        return max_length

# Example usage
s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))  # Output: 3
