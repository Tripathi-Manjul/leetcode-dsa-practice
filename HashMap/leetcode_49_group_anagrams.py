from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups a set of words into anagram clusters using a frequency-vector
        hashing strategy.

        Explanation of the key design decisions:
        ----------------------------------------

        1. Frequency Vector as Signature:
           Each word is transformed into a 26-length frequency vector representing
           the counts of characters 'a' through 'z'. Two words are anagrams if and
           only if their frequency vectors are identical.

        2. Why the key must be a tuple, not a list:
           - Python dictionary keys must be hashable, which requires immutability.
           - Lists are mutable, so they are not hashable and cannot be used as keys.
           - Tuples are immutable and hashable; therefore the frequency list must be
             converted to a tuple before being used as a dictionary key.

             Example:
               freq = [1,0,0,...]     # Not hashable → invalid as a dictionary key
               tuple(freq)            # Hashable → valid key

           Using tuple(freq) ensures that all words with identical character
           distributions map to the same dictionary key.

        3. Why defaultdict(list) is used:
           defaultdict(list) automatically initializes an empty list for any new key.
           This eliminates the need for conditional checks such as:
               if key not in map: map[key] = []
           and simplifies the grouping logic.

        4. Output:
           The dictionary values contain lists of grouped anagrams. Returning
           list(map.values()) produces the required list of lists.


        Complexity:
        -----------
        Let n be the number of strings and m be the maximum length of a string.

        Time:  O(n * m)      # Building the frequency vector for each string
        Space: O(n * m)      # Storing all frequency signatures and grouped words
        """

        # Map: (frequency signature) → list of anagrams
        groups = defaultdict(list)

        for word in strs:
            # Build frequency vector for 'a' to 'z'
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            # Convert frequency list to tuple so it becomes hashable
            signature = tuple(freq)

            # Append the word to its anagram group
            groups[signature].append(word)

        # Convert the dictionary values to a list of lists
        return list(groups.values())
