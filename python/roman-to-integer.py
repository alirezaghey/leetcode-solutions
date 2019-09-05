#  https://leetcode.com/problems/roman-to-integer/
#  Related Topics: Math, String, Hash Table
#  Difficulty: Easy


# Initial thoughts:
# We are going to create a lookup table for every combination of Roman numbers
# Since there are both two-letter and one-letter combinations, looping over the
# input string, we first check for the two-letter combination in the lookup and
# if it's not there, we take the one-letter combination, all the way adding the
# values to the result.

# Time complexity: O(n) we have to look at each character in the input string
# Space complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        lookup = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000,
                  "IV": 4,
                  "IX": 9,
                  "XL": 40,
                  "XC": 90,
                  "CD": 400,
                  "CM": 900}
        i = 0
        while i < len(s):
            if i < len(s)-1 and s[i:i+2] in lookup:
                result += lookup[s[i:i+2]]
                i += 2
            else:
                result += lookup[s[i]]
                i += 1
        return result
