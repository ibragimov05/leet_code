class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        return "".join(s[(i + (k % n)) % n] for i in range(n))
