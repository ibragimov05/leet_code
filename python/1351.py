class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        negative_numbers: int = 0

        for i in grid:
            for j in range(len(i) - 1, -1, -1):
                if i[j] < 0:
                    negative_numbers += 1
                else:
                    break

        return negative_numbers
