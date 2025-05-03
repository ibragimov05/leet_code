from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count: set[int] = set()

        for s in sentences:
            count.add(len(s.split()))

        return max(count)
