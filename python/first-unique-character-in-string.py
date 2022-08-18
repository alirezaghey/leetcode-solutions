from collections import Counter


class Solution:
    # TC: O(n) where n is the length of s
    # SC: O(n)
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for i, el in enumerate(s):
            if counter[el] == 1:
                return i
        return -1
