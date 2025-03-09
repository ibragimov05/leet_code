class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        res = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(f"{start}")
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        if start == nums[-1]:
            res.append(f"{start}")
        else:
            res.append(f"{start}->{nums[-1]}")

        return res
