class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        seen = set()
        sneaky_numbers = set()

        for number in nums:
            if number in seen and number not in sneaky_numbers:
                sneaky_numbers.add(number)
                if len(sneaky_numbers) == 2:
                    return list(sneaky_numbers)
            seen.add(number)

        return list(sneaky_numbers)
