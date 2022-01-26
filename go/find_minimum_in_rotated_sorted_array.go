package leetcode

// Time complexity: O(log n) where n is the length of nums
// Space complexity: O(1)
func findMin(nums []int) int {
	if nums[0] < nums[len(nums)-1] || len(nums) == 1 {
		return nums[0]
	}

	left, right, res := 0, len(nums)-1, nums[0]

	for left <= right {
		mid := left + (right-left)/2

		if nums[mid] < nums[0] { // right side
			res = min(res, nums[mid])
			right = mid - 1
		} else { // left side
			left = mid + 1
		}
	}
	return res
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
