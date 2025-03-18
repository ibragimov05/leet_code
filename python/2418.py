from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        people.sort(reverse=True, key=lambda x: x[1])
        return [name[0] for name in people]
