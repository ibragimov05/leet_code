from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        not_lost_match: List[int] = []
        one_lost_match: List[int] = []

        tracker: dict[int, int] = {}

        for match in matches:
            tracker[match[0]] = tracker.get(match[0], 0)
            tracker[match[1]] = tracker.get(match[1], 0) + 1

        for player, lose_count in tracker.items():
            if lose_count > 1:
                continue

            if lose_count == 1:
                one_lost_match.append(player)
            elif lose_count == 0:
                not_lost_match.append(player)

        return [sorted(not_lost_match), sorted(one_lost_match)]
