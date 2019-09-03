#  Related Topics: Math
#  Difficulty: Easy

# Initial thoughts:
# The easiest way to solve this is by taking one digit at a time from the end of
# our input and add it to the result using basic math reversing the number in the process
# One problem that we need to watch out for is that if the number
# doesn't fit in a 32-bit signed integer, we need to return 0;
# Python default
# we can define a MAX and MIN and if the result is greater or less
# than MAX and MIN return 0.
# This approach has a time complexity of O(log n), the number of digits,
# and a space complexity of O(log n), because we define character for every digit.

# Optimization:
# A more effective method is to use math to solve the problem. The traditional push
# and pop on arrays can be simulated on numbers by using employing basic arithmetic.


# Time complexity: O(log n) because x has approximately log10(n) digits
# Space complexity: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        MAX = 2**31-1
        MIN = -2**31

        neg = False
        if x < 0:
            neg = True
            x = x * -1
        while(x > 0):
            result = result*10 + x % 10
            x = x // 10

            if not neg and result > MAX:
                return 0
            elif neg and result*-1 < MIN:
                return 0
        return result if not neg else result*-1
