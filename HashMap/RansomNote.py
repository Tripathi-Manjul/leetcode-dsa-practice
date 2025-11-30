# Solution 1: Using Python's built-in Counter (clean, concise)
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determines if the ransomNote can be constructed from the characters in magazine.
        Each character in magazine can only be used once.

        Time Complexity: O(n + m), where n = len(ransomNote), m = len(magazine)
        Space Complexity: O(1) — at most 26 lowercase letters are tracked
        """

        # Count the frequency of each character in magazine
        magazine_count = Counter(magazine)

        # Count the frequency of each character needed in ransomNote
        ransom_count = Counter(ransomNote)

        # For each character in the ransom note, check if magazine provides enough occurrences
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                # Not enough characters available in magazine
                return False

        # All required characters are available in sufficient quantity
        return True

# Solution 2: Manual frequency map using dict.get()
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Checks whether the ransomNote can be constructed using characters from magazine.
        Each character in magazine can only be used once.

        Time Complexity: O(n + m) where
            n = length of magazine (to build frequency map),
            m = length of ransomNote (to check availability)
        Space Complexity: O(1) — bounded by number of unique lowercase letters (26 max)
        """

        freq_map = {}

        # Count the frequency of each character in magazine
        for char in magazine:
            # Use dict.get to handle missing keys and increment count
            freq_map[char] = freq_map.get(char, 0) + 1

        # For each character in ransomNote, check if it is available in freq_map
        for char in ransomNote:
            # If character exists and count is positive, use one occurrence
            if char in freq_map and freq_map[char] > 0:
                freq_map[char] -= 1
            else:
                # Character either not in magazine or used up already
                return False

        # All characters in ransomNote are sufficiently available in magazine
        return True

# Solution 3: Single Hashmap Used
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Step 1: Build a frequency map of magazine characters.
        # Counter creates a hash map where:
        # key = character, value = number of times it appears in magazine.
        # We only need this, because ransomNote will be validated against it.
        mag_count = Counter(magazine)

        # Step 2: Iterate through each character in ransomNote.
        # We avoid building Counter for ransomNote to reduce extra memory usage
        # and demonstrate efficient constraint handling in interviews.
        for char in ransomNote:

            # Step 3: Check if the current character is available in magazine frequency map.
            # If value is 0, it means either:
            # (a) the char never existed in magazine, or
            # (b) it existed but has already been fully used once.
            if mag_count[char] == 0:
                return False  # Cannot construct ransomNote as this char is exhausted.

            # Step 4: Decrement frequency since each character can only be used once.
            # This ensures we respect the single-use constraint.
            mag_count[char] -= 1

        # Step 5: If all characters passed availability checks, return True.
        return True

 