#  https://leetcode.com/problems/bulb-switcher/
#  Related Topics: Math, Brainteaser
#  Difficulty: Medium


# Time complexity: O(sqrt(n)) where n is the number of nodes in the Linked List
# Space complexity: O(1)
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        count = 0
        i = 1
        while i*i <= n:
            count += 1
            i += 1
        return count

    # def bulbSwitch(self, n: int) -> int:
    #     return math.floor(math.sqrt(n))
