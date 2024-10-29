class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_count = 0
        for stone in stones:
            if stone in jewels:
                jewels_count += 1
        return jewels_count
