from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for num in matrix:
            for digit in num:
                if digit == target:
                    return True
        return False
