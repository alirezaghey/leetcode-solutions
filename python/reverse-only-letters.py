#  https://leetcode.com/problems/reverse-only-letters/
#  Related Topics: String
#  Difficulty: Easy


# Initial thoughts:
# Using two pointer at the beginning and end of the string we check
# whether they are a letter or not. If any of them is not a letter we
# only move that character to the inside of the array, if not we swapp
# the letters at thos character and move both of them to the inside.
# Repeat until the two pointers meet.

# Time complexity: O(n) where n === the length of S
# Space complexity: O(n) where n === the length of S (the auxilliary space is actually because string are immutable in python)

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left = 0
        right = len(S)-1
        arrS = list(S)
        while left < right:
            if not arrS[left].isalpha():
                left += 1
                continue
            if not arrS[right].isalpha():
                right -= 1
                continue
            arrS[left], arrS[right] = arrS[right], arrS[left]
            left += 1
            right -= 1
        return "".join(arrS)
