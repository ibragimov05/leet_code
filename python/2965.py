from collections import Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        all_nums: list[int] = [num for row in grid for num in row]
        count = Counter(all_nums)

        repeated: int = next(num for num, count in count.items() if count == 2)

        all_nums_set = set(all_nums)

        n = len(grid)
        for index in range(1, n * n + 1):
            if index not in all_nums_set:
                return [repeated, index]

        return [repeated, -1]
