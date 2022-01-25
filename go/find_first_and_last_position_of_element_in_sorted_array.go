package leetcode

// Time complexity: O(log n) where n is the length of nums
// Space complexity: O(1)
func searchRange(nums []int, target int) []int {
	bisectLeft := func(arr []int, target int) int {
		left, right := 0, len(arr)

		for left < right {
			mid := left + (right-left)/2

			if target > arr[mid] {
				left = mid + 1
			} else {
				right = mid
			}
		}
		return left
	}

	bisectRight := func(arr []int, target int) int {
		left, right := 0, len(arr)

		for left < right {
			mid := left + (right-left)/2

			if target < arr[mid] {
				right = mid
			} else {
				left = mid + 1
			}
		}
		return left
	}

	if len(nums) == 0 {
		return []int{-1, -1}
	}

	left := bisectLeft(nums, target)
	if left >= len(nums) || nums[left] != target {
		return []int{-1, -1}
	}

	right := bisectRight(nums, target)
	return []int{left, right - 1}
}
