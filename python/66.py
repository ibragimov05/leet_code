class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        res_str = str(int("".join(map(str, digits))) + 1)

        result: list[int] = []
        
        for i in res_str:
            result.append(int(i))
            
        return result
