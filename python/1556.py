class Solution:
    def thousandSeparator(self, n: int) -> str:
        str_n = str(n)

        parts = []
        for i in range(len(str_n), 0, -3):
            start = max(0, i - 3)
            parts.append(str_n[start:i])

        return ".".join(reversed(parts))
