class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = []

        for i in range(len(prices) - 1):
            did_add = False
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    res.append(prices[i] - prices[j])
                    did_add = True
                    break
            if not did_add:
                res.append(prices[i])

        res.append(prices[-1])
        return res
