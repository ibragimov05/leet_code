class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = heights.copy()
        expected.sort()

        return sum(1 for i in range(len(expected)) if expected[i] != heights[i])
