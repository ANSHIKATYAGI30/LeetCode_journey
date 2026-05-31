class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        word_count = Counter(words)
        result = []

        # Try each possible offset
        for i in range(word_len):

            left = i
            curr_count = {}
            count = 0

            # Move window in steps of word_len
            for right in range(i, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                # Valid word
                if word in word_count:

                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1

                    # Too many occurrences -> shrink window
                    while curr_count[word] > word_count[word]:

                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Found valid concatenation
                    if count == total_words:
                        result.append(left)

                else:
                    # Reset window
                    curr_count = {}
                    count = 0
                    left = right + word_len

        return result
