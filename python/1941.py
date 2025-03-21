class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = s.count(s[0])
        for i in range(1, len(s)):
            if s.count(s[i]) != count:
                return False
        return True
