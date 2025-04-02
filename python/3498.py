class Solution:
    def reverseDegree(self, s: str) -> int:
        reversed_degree: int = 0

        for i in range(len(s)):
            reversed_degree += (26 - (ord(s[i]) - ord("a"))) * (i + 1)

        return reversed_degree
