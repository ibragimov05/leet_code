class Solution:
    def isBalanced(self, num: str) -> bool:
        odd_numbers: list[int] = [int(num[i]) for i in range(len(num)) if i % 2 != 0]
        even_numbers: list[int] = [int(num[i]) for i in range(len(num)) if i % 2 == 0]

        return sum(odd_numbers) == sum(even_numbers)
