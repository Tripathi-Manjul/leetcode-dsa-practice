from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Problem:
        --------
        Given an array of strings, group the anagrams together.
        Return the groups in any order.

        An anagram is a word formed by rearranging the letters of another word.
        Example: "eat", "tea", "ate" are all anagrams.

        Approach:
        ---------
        - Use a hashmap (dictionary) where:
          Key   = a signature that uniquely identifies an anagram group
          Value = list of words belonging to that group

        - For the key, instead of sorting (O(m log m)), we use a 
          fixed-size frequency count of characters (O(m)).

          Example:
          word = "eat"
          count array = [1, 0, 0, ..., 1, 0, ..., 1, 0 ...] 
                        (1 for 'a', 1 for 'e', 1 for 't')

        - Convert this count array into a tuple (immutable, hashable),
          and use it as a dictionary key.

        - Append the original word into the dictionary entry.

        - Finally, return the dictionary values as a list of lists.

        Complexity:
        -----------
        n = number of words, m = max length of a word

        Time:  O(n * m)   # counting characters for each word
        Space: O(n * m)   # storing frequency signatures + groups
        """

        # dictionary where key = tuple(counts), value = list of words
        res = defaultdict(list)

        for s in strs:
            # Step 1: Build frequency count for each word
            count = [0] * 26  # 26 lowercase English letters
            for c in s:
                count[ord(c) - ord("a")] += 1

            # Step 2: Convert to tuple (hashable) and use as key
            res[tuple(count)].append(s)

        # Step 3: Convert dict_values object to list before returning
        return list(res.values())
