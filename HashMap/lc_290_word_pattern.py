class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Determines whether a given string of words follows the same pattern
        defined by a sequence of characters.

        zip usage:
        ----------
        zip(pattern, words) pairs elements from both sequences so that each
        iteration gives (pattern_char, corresponding_word). This allows clean,
        parallel traversal without manual indexing.
        """

        # Split input string into words
        words = s.split()

        # If lengths do not match, a bijection is impossible
        if len(pattern) != len(words):
            return False

        char_to_word = {}  # mapping: pattern character → word
        word_to_char = {}  # mapping: word → pattern character

        # Iterate over pattern characters and words in parallel using zip
        # Example:
        # pattern = "abba"
        # words   = ["dog", "cat", "cat", "dog"]
        # zip yields:
        # ('a', 'dog'), ('b', 'cat'), ('b', 'cat'), ('a', 'dog')
        for ch, w in zip(pattern, words):

            # Check or establish mapping from character to word
            if ch in char_to_word:
                if char_to_word[ch] != w:
                    return False
            else:
                char_to_word[ch] = w

            # Check or establish mapping from word to character
            if w in word_to_char:
                if word_to_char[w] != ch:
                    return False
            else:
                word_to_char[w] = ch

        return True
