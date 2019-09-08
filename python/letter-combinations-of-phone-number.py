# https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/
#  Related Topics: String, Backtracking
#  Difficulty: Medium

# Time complexity: O(3^n * 4^m) where n === number of digits that have 3 corresponding chars and
# m === numer of digits that have 4 corresponding chars
# Space complexit: O(3^n * 4^m)


from typing import List, Dict


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"}

        result = []

        self.permute("", digits, result, lookup)
        return result

    def permute(self, combination: str, remaining: str, result: List[str], lookup: Dict[int, str]):
        if len(remaining) == 0:
            result.append(combination)
            return
        for letter in lookup[int(remaining[0])]:
            self.permute(combination+letter, remaining[1:], result, lookup)
