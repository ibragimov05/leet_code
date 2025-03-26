from typing import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i, char in enumerate(count):
            if count[char] == 1:
                return i
        return -1


# print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
# print(Solution().firstUniqChar("aabb"))
