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
