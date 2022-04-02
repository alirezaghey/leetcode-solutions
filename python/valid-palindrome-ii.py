class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def validPalindrome(self, s: str) -> bool:
        def check(left, right, found=False):
            while left < right:
                if s[left] == s[right]:
                    left, right = left+1, right-1
                elif found == False:
                    return check(left+1, right, True) or check(left, right-1, True)
                else:
                    return False
            return True

        return check(0, len(s)-1)
