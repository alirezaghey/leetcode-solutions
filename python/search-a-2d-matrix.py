from typing import List
#  https://leetcode.com/problems/search-a-2d-matrix/
#  Related Topics: Array, Binary Search
#  Difficulty: Medium


# Initial thoughts:
# Since each row of the matrix is sorted and the first element of each row
# is larger than the last element of the previous row, we can find out whether
# our target element is available by first performing a binary search on the rows
# of the matrix. If we find a potential row that could possibly harbor our target
# we are going to perform a binary search on the cells on that specific row.
# Such a row must have the following properties: row[0] <= target and row[-1] >= target

# Time Complexity: O(log(n) + log(m)) where n == len(matrix) and m == len(matrix[0])
# Space Complexity: O(1)

class Solution:
    # Time complexity: O(log n + log m)
    # where n is the number of rows and m the number of cols in matrix
    # Space complexity: O(1)
    # Arguably a cleaner version than further below
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row(matrix, target):
            left, right = 0, len(matrix)-1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if matrix[mid][0] > target:
                    right = mid-1
                elif matrix[mid][-1] < target:
                    left = mid+1
                else:
                    return mid
            return -1
        
        def find_el(arr, target):
            left, right = 0, len(arr)-1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if target < arr[mid]:
                    right = mid-1
                elif target > arr[mid]:
                    left = mid+1
                else:
                    return mid
            return -1
        
        row_idx = find_row(matrix, target)
        if row_idx == -1: return False
        
        el_idx = find_el(matrix[row_idx], target)
        
        if el_idx == -1: return False
        return True


    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not len(matrix) or not len(matrix[0]):
            return False

        row = None
        left, right = 0, len(matrix)-1

        while left <= right:
            mid = (right-left)//2 + left
            if target < matrix[mid][0]:
                right = mid-1
            elif target > matrix[mid][-1]:
                left = mid+1
            else:
                row = mid
                break

        if row == None:
            return False

        left, right = 0, len(matrix[0])-1

        while left <= right:
            mid = (right-left)//2 + left
            if target < matrix[row][mid]:
                right = mid-1
            elif target > matrix[row][mid]:
                left = mid+1
            else:
                return True

        return False
