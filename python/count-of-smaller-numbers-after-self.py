class Solution:
    # using a custom merge sort algorithm
    def countSmaller(self, nums: List[int]) -> List[int]:
        def divide(l, h, nums, res):
            if l >= h:
                return
            
            m = l + (h - l) // 2
            divide(l, m, nums, res)
            divide(m+1, h, nums, res)
            
            i, j = l, m+1
            
            while i <= m:
                while j <= h and nums[j][1] < nums[i][1]: j += 1
                res[nums[i][0]] += max(j - m - 1, 0)
                i += 1
            
            merge(l, m, h, nums)
            
        def merge(l, m, h, nums):
            temp = nums[l: m+1]
            
            i, j, k = 0, m+1, l
            while i < len(temp) and j <= h:
                if temp[i][1] <= nums[j][1]:
                    nums[k] = temp[i]
                    i += 1
                else:
                    nums[k] = nums[j]
                    j += 1
                k += 1
            
            while i < len(temp):
                nums[k] = temp[i]
                i, k = i+1, k+1
            while j <= h:
                nums[k] = nums[j]
                j, k = j+1, k+1
                
        nums = [(i, el) for i, el in enumerate(nums)]
        res = [0]*len(nums)
        divide(0, len(nums)-1, nums, res)
        return res

from sortedcontainers import SortedList
class Solution2:
    # using a SortedList from sortedcontainers
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        res = []
        for i in range(len(nums)-1, -1, -1):
            idx = sl.bisect_left(nums[i])
            sl.add(nums[i])
            res.append(idx)
        return list(reversed(res))