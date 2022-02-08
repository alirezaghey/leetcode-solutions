class Solution:
    # Time complexity: O(log num)
    # Space complexity: O(1)
    def addDigits(self, num: int) -> int:
        def add(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res
        while num > 9:
            num = add(num)
        return num