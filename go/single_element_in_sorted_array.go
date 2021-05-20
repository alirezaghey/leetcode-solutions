package leetcode

func singleNonDuplicate(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	left, right := 0, len(nums)-1

	for left <= right {
		mid := left + (right-left)/2

		if mid > 0 && mid < len(nums)-1 {
			if nums[mid] != nums[mid-1] && nums[mid] != nums[mid+1] {
				return nums[mid]
			}
		} else if mid == 0 && nums[mid] != nums[mid+1] {
			return nums[mid]
		} else if mid == len(nums)-1 && nums[mid] != nums[mid-1] {
			return nums[mid]
		}

		if mid%2 == 0 { // both sides have even number of elements
			if nums[mid] != nums[mid-1] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		} else {
			if nums[mid] == nums[mid-1] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}
	return 0
}
