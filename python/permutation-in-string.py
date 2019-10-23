#  https://leetcode.com/problems/permutation-in-string/
#  Related Topics: Two Pointers, Sliding Window, Hash Table
#  Difficulty: Medium


# Initial thoughts:
# Creating a frequency table for the characters in s1 we are going to
# have a changing frequency table for s2 that encompasses chracters equal
# to the length of s1. Moving forward with the freq table on s2, we are going
# to compare the two freq tables at each step. If they are identical, we have a
# permutation of s1 in s2.
# Since we are dealing with a predefined set of characters (in this case English
# small letters) the comparision of the freq tables takes constant time (26 at most)
# Creating the freq tables also won't take more than linear time equal to the length
# of s2.

# Time complexity: O(n) where n == len(s2)
# Space complexity: O(1) because the freq tables won't have more than 26 chars
from typing import List
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def createFreqTable(s: str) -> {str: int}:
            dic = defaultdict(int)
            for c in s:
                dic[c] += 1
            return dic

        dic1 = createFreqTable(s1)
        dic2 = createFreqTable(s2[0:len(s1)])
        if dic1 == dic2:
            return True
        for i in range(len(s1), len(s2)):
            dic2[s2[i-len(s1)]] -= 1
            if dic2[s2[i-len(s1)]] == 0:
                del dic2[s2[i-len(s1)]]
            dic2[s2[i]] += 1
            if dic2 == dic1:
                return True
        return False
