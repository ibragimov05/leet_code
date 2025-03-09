class Solution:
    def calPoints(self, operations: list[str]) -> int:
        points: list[int] = []

        for op in operations:
            if op.isdigit():
                points.append(int(op))
            elif op == "C":
                points.pop()
            elif op == "D":
                nums: list[int] = []

                for j in range(operations.index(op) - 1, -1, -1):
                    if operations[j].isdigit():
                        nums.append(int(operations[j]))
                    if len(nums) == 2:
                        break

                points.append(nums[0] * nums[1])
            elif op == "+":
                points.append(points[-1] + points[-2])

        return sum(points)


print(Solution().calPoints(["5", "2", "C", "D", "+"]))
print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(Solution().calPoints(["1", "C"]))

# Example 1:

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

# Example 2:

# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

# Example 3:

# Input: ops = ["1","C"]
# Output: 0
# Explanation:
# "1" - Add 1 to the record, record is now [1].
# "C" - Invalidate and remove the previous score, record is now [].
# Since the record is empty, the total sum is 0.
