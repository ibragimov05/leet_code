class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res: list[str] = []

        for index in range(0, len(s), k):
            box = sum(ord(char) - 97 for char in s[index : index + k])
            res.append(chr(box % 26 + 97))

        return "".join(res)
