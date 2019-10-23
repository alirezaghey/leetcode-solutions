#  https://leetcode.com/problems/valid-anagram/
#  Related Topics: Hash Table, Sort
#  Difficulty: Easy


# Initial thoughts:
# For a word to be an anagram of another word, it must have the exact
# same characters with the same quanitity as the other word, just in a
# different ordering.
# Using a hash map, we can create a frequency table from the first word
# and remove them from the frequency table while we go through the second
# word.
# If at the end the frequency table is empty, we have an anagram

# Time complexity: O(n) where n == len(s)
# Space complexity: O(1) because the freq tables won't have more than 26 chars
# (even if we were dealing with the whole unicode spectrum, it would be of constant
# complexity)
from typing import List
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            if c in dic:
                if dic[c] == 1:
                    del dic[c]
                else:
                    dic[c] -= 1
            else:
                return False
        return len(dic) == 0
