package leetcode

// Time complexity: O(log n + log m) where n and m are the Nr. of rows and cols in the matrix
// Space complxity: O(1)
func searchMatrix(matrix [][]int, target int) bool {
	findRow := func(matrix [][]int, target int) int {
		left, right := 0, len(matrix)-1

		for left <= right {
			mid := left + (right-left)/2

			if matrix[mid][0] > target {
				right = mid - 1
			} else if matrix[mid][len(matrix[0])-1] < target {
				left = mid + 1
			} else {
				return mid
			}
		}
		return -1
	}

	findEl := func(arr []int, target int) int {
		left, right := 0, len(arr)-1

		for left <= right {
			mid := left + (right-left)/2

			if target < arr[mid] {
				right = mid - 1
			} else if target > arr[mid] {
				left = mid + 1
			} else {
				return mid
			}
		}
		return -1
	}

	rowIdx := findRow(matrix, target)
	if rowIdx == -1 {
		return false
	}

	elIdx := findEl(matrix[rowIdx], target)
	if elIdx == -1 {
		return false
	}
	return true
}
