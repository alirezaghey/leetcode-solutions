from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr, total, res = 0, 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g-c
            curr += g-c
            if curr < 0:
                curr = 0
                res = i+1
        if total < 0:
            return -1
        else:
            return res
        
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # Time limit exceeded
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        # if sum(gas) < sum(cost): return -1
        
        for i in range(len(gas)):
            curr = gas[i] - cost[i]
            if curr < 0: continue
                
            j = (i+1) % len(gas)
            while j != i:
                curr += gas[j] - cost[j]
                if curr < 0:
                    break
                j = (j+1) % len(gas)
            if j == i:
                return i
        return -1