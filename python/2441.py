class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        box = nums.copy()
        for i in range(len(nums)):
            max_num = max(box)
            if max_num * -1 in nums:
                return max_num
            else:
                box.remove(max_num)
        return -1
