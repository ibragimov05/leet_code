class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split("-")

        return f"{self._to_binary_(int(year))}-{self._to_binary_(int(month))}-{self._to_binary_(int(day))}"

    def _to_binary_(self, number: int) -> str:
        bin = ""

        while number > 0:
            bin = str(number % 2) + bin
            number = number // 2

        return bin


s = Solution()
print(s.convertDateToBinary("2080-02-29"))

# Input: date = "2080-02-29"
# Output: "100000100000-10-11101"
# Explanation:
# 100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.
