from typing import List
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(
            len(list(filter(lambda x: x%2 == 0, position))),
            len(list(filter(lambda x: x%2 == 1, position)))
        )