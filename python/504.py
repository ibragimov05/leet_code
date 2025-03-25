class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        base_7: list[str] = []

        sign: str = "-" if num < 0 else ""

        num = abs(num)

        while num > 0:
            base_7.append(str(num % 7))
            num //= 7

        return sign + "".join(reversed(base_7))
