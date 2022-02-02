#  https://leetcode.com/problems/find-all-anagrams-in-a-string/
#  Related Topics: Two Pointers, Sliding Window, Hash Table
#  Difficulty: Medium


# Initial thoughts:
# Creating a frequency table for the characters in p we are going to
# have a changing frequency table for s that encompasses chracters equal
# to the length of p. Moving forward with the freq table on s, we are going
# to compare the two freq tables at each step. If they are identical, we have an
# anagram of p in s and we are going to save the anagram's index in s in a result array.
# Since we are dealing with a predefined set of characters (in this case English
# small letters) the comparison of the freq tables takes constant time (26 at most)
# Creating the freq tables also won't take more than linear time equal to the length
# of s.

# Time complexity: O(n) where n == len(s)
# Space complexity: O(1) because the freq tables won't have more than 26 chars
from typing import List, Dict
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        def createFreqTable(s: str) -> Dict[str, int]:
            dic = defaultdict(int)
            for c in s:
                dic[c] += 1
            return dic

        dicP = createFreqTable(p)
        dicS = createFreqTable(s[0:len(p)])

        res = []
        if dicP == dicS:
            res.append(0)

        for i in range(len(p), len(s)):
            dicS[s[i]] += 1
            if dicS[s[i-len(p)]] == 1:
                del dicS[s[i-len(p)]]
            else:
                dicS[s[i-len(p)]] -= 1
            if dicS == dicP:
                res.append(i-len(p)+1)
        return res
