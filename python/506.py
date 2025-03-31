from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score: List[int] = sorted(score[:], reverse=True)
        ranks: List[str] = []

        for i in range(len(score)):
            index: int = sorted_score.index(score[i])
            value: str = ""

            if index == 0:
                value = "Gold Medal"
            elif index == 1:
                value = "Silver Medal"
            elif index == 2:
                value = "Bronze Medal"
            else:
                value = str(index + 1)

            ranks.append(value)

        return ranks
