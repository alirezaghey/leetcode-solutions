from typing import List

class Solution:
    # TC: O(n)
    # SC: O(n)
    # optimized to avoid creating auxiliary space to keep track of visited nodes
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0: return True
        N = len(arr)
        stack = [(start, arr[start])]
        arr[start] = -1
        
        while stack:
            i, d = stack.pop()
            forward, backward = i+d, i-d
            
            if forward < N and arr[forward] != -1:
                if arr[forward] == 0:
                    return True
                stack.append((forward, arr[forward]))
                arr[forward] = -1
            if backward >= 0 and arr[backward] != -1:
                if arr[backward] == 0:
                    return True
                stack.append((backward, arr[backward]))
                arr[backward] = -1
        return False
        
    # TC: O(n)
    # SC: O(n)
    def canReach2(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0: return True
        N = len(arr)
        dp = [False]*(N)
        dp[start] = True
        stack = [(start, arr[start])]
        
        while stack:
            i, d = stack.pop()
            if i + d < N and dp[d+i] == False:
                ni = i + d
                if arr[ni] == 0:
                    return True
                stack.append((ni, arr[ni]))
                dp[ni] = True
            if i - d >= 0 and dp[i-d] == False:
                ni = i - d
                if arr[ni] == 0:
                    return True
                stack.append((ni, arr[ni]))
                dp[ni] = True
        return False
        