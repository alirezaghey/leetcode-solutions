class Solution:
    # Time complexity: O(n) where n is the length of the input string
    # Space complexity: O(1)
    def reverseWords(self, s: str) -> str:
        def reverse(l, r, arr):
            N = len(arr)
            for i in range((r-l+1) // 2):
                arr[l+i], arr[r-i] = arr[r-i], arr[l+i]
        
        s = list(s)
        l = -1
        for r in range(len(s)):
            if r == len(s)-1 or s[r+1] == " ":
                if l == -1:
                    l = r
                reverse(l, r, s)
                l = -1
            elif s[r] != " " and l == -1:
                l = r
        return "".join(s)
        
    # Time complexity: O(n) where n is the length of the input string
    # Space complexity: O(n)
    def reverseWords2(self, s: str) -> str:
        return " ".join("".join(list(reversed(word))) for word in s.split(" "))