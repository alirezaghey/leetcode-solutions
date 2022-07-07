from functools import lru_cache


class Solution:
    # Memoized recursive approach
    # TC: O(n * m) where n and m are the length of s1 and s2
    # SC: O(n * m)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(None)
        def dfs(n1, n2, n3):
            if n3 >= len(s3):
                return True

            s1_res, s2_res = False, False

            if n1 < len(s1) and s1[n1] == s3[n3]:
                s1_res = dfs(n1+1, n2, n3+1)
            if s1_res:
                return True

            if n2 < len(s2) and s2[n2] == s3[n3]:
                s2_res = dfs(n1, n2+1, n3+1)
            return s2_res

        return dfs(0, 0, 0)
