class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        res: list[int] = []

        for i in matrix:
            minimum = min(i)
            index_min = i.index(minimum)
            print(f"{minimum} : {index_min}")
        return res
