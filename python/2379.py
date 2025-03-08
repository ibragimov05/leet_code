class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ls: list[int] = []

        for i in range(len(blocks) - k + 1):
            ls.append(blocks[i : i + k].count("W"))

        return min(ls)
