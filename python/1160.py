from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_count = Counter(chars)
        res = 0

        for word in words:
            word_count = Counter(word)
            if all(word_count[char] <= char_count[char] for char in word_count):
                res += len(word)

        return res
