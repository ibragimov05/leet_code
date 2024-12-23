class Solution:
    def findLucky(self, arr: list[int]) -> int:
        return max([i for i in set(arr) if (arr.count(i)) == i], default=-1)
