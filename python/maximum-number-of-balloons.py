#  https://leetcode.com/problems/maximum-number-of-balloons/
#  Related Topics: Hash Table, String
#  Difficulty: Easy


# Initial thoughts:
# Using a hash table we are going to count the frequency of the letters
# b,a,l,o, and n. Taking the floor division of the letters l and o
# (because we need two of them of the word balloon) we are going to take
# the minium number in the values of the frequency table.

# Time complexity: O(n) where n === len(text)
# Space complexity: O(1)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        fTable = {char: 0 for char in 'balon'}
        for char in text:
            if char in fTable:
                fTable[char] += 1
        fTable['l'] = fTable['l']//2
        fTable['o'] = fTable['o']//2

        return min(fTable.values())
