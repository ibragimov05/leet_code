from typing import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_chars: list[str] = sorted(s, key=lambda x: (count[x], x), reverse=True)
        return "".join(sorted_chars)
