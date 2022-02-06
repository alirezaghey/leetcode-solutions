package leetcode

// Time complexity: O(n) where n is the length of nums.
// Space complexity: O(1)
// Two pointer approach.
func removeDuplicates(nums []int) int {
	if len(nums) < 3 {
		return len(nums)
	}
	left := 2
	for i := 2; i < len(nums); i++ {
		if nums[left-2] != nums[i] {
			nums[left] = nums[i]
			left += 1
		}
	}
	return left
}
