from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_strings: int = 0

        for word in words:
            if all([letter in allowed for letter in word]):
                consistent_strings += 1

        return consistent_strings
