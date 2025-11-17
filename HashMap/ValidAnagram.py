"""
Valid Anagram Solutions (Python)
This file contains two implementations commonly discussed in technical interviews:
1. Counter-based solution (Pythonic, concise)
2. Frequency-array solution (preferred for interviews, optimal and low-level)

Each method is fully commented for clear understanding.
"""

from collections import Counter


class SolutionCounter:
    """
    Approach 1: Using Python's Counter

    Rationale:
    - Very concise and uses Python's standard library.
    - Counter creates a hash map of character frequencies.
    - Two strings are anagrams if and only if their frequency maps are equal.

    Time Complexity: O(n)
    Space Complexity: O(1) for fixed lowercase alphabet
    """

    def isAnagram(self, s: str, t: str) -> bool:
        # Direct comparison of character frequency dictionaries
        return Counter(s) == Counter(t)


class SolutionFrequencyArray:
    """
    Approach 2: Explicit Frequency Array (Preferred for interviews)

    Rationale:
    - Demonstrates understanding of frequency counting without library abstractions.
    - Uses an integer array of size 26 (for lowercase English letters).
    - Increment counts for characters in s and decrement for characters in t.
    - If all counts return to zero, the strings are anagrams.

    Time Complexity: O(n)
    Space Complexity: O(1) because array size is fixed
    """

    def isAnagram(self, s: str, t: str) -> bool:
        # Quick length check: unequal lengths cannot be anagrams
        if len(s) != len(t):
            return False

        # Frequency array for 26 lowercase letters
        freq = [0] * 26

        # Increase counts for characters in s
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Decrease counts for characters in t
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1

        # If all counts are zero, both strings had identical frequencies
        for count in freq:
            if count != 0:
                return False

        return True


# Example execution for testing both implementations
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    print("Testing Counter-based implementation:")
    sol1 = SolutionCounter()
    print(sol1.isAnagram(s, t))  # Expected True

    print("\nTesting Frequency-array implementation:")
    sol2 = SolutionFrequencyArray()
    print(sol2.isAnagram(s, t))  # Expected True
