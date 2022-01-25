package leetcode

// Time complexity: O(log n) where n is the length of nums
// Space complexity: O(1)
func search(nums []int, target int) int {
	left, right := 0, len(nums)-1

	for left <= right {
		mid := left + (right-left)/2

		if target > nums[mid] {
			if nums[mid] < nums[0] { // right
				if target < nums[0] {
					left = mid + 1
				} else {
					right = mid - 1
				}
			} else { // left
				left = mid + 1
			}
		} else if target < nums[mid] {
			if nums[mid] < nums[0] { // right
				right = mid - 1
			} else { // left
				if target < nums[0] {
					left = mid + 1
				} else {
					right = mid - 1
				}
			}
		} else {
			return mid
		}
	}
	return -1
}
