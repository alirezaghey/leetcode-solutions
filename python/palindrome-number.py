#  https://leetcode.com/problems/palindrome-number/
#  Related Topics: Math, Array
#  Difficulty: Easy


# Initial thoughts:
# Converting the number to an array of strings
# we can reverse the array and check whether it
# equals the original.

# Time complexity: O(log n) because x has approximately log10(n) digits
# Space complexity: O(log n) because we need to convert the number to a string


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[len(x)-1-i]:
                return False
        return True


# Optimization:
# Considering the fact that we just need to compare the head-half
# to the tail-half to make sure it's a palindrome, it's enough to
# just loop over the floor of the half of the int converted to string.
# If the int has odd number of digits, it does not make any difference
# what the middle digit is.

# Time complexity: O(log n) because x has approximately log10(n) digits
# Space complexity: O(log n) because we need to convert the number to a string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[len(x)-1-i]:
                return False
        return True

# Optimization:
# Using basic math we can revert the number without converting it to a string
# Normally, we would risk running into an overflow and would have had to take
# care of that, but Python numbers are dynamic and never overflow.
# This method will render our space complexity constant.

# Time complexity: O(log n) because x has approximately log10(n) digits
# Space complexity: O(1) because we need to convert the number to a string


class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev, tempX = 0, x
        while tempX > 0:
            rev = rev * 10 + tempX % 10
            tempX = tempX // 10
        return rev == x
