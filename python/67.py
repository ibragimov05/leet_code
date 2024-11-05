class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res_sum = int(a) + int(b)

        
        return self._to_binary_(res_sum)
    
    def _to_binary_(self, number: int) -> str:
        bin = ""

        while number > 0:
            bin = str(number % 2) + bin
            number = number // 2

        return bin



s = Solution()
print(s.addBinary("11", "1"))

