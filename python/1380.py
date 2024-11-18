class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        res: list[int] = []

        for i in matrix:
            minimum = min(i)
            index_min = i.index(minimum)
            # for j in range(len(i)):
            print(f"{minimum} : {index_min}")
        return res


s = Solution()
print(s.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(s.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
