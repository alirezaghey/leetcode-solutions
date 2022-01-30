package leetcode

// Time complexity: O(n) where n is the length of nums
// Space complexity: O(1)
func rotate(nums []int, k int) {
	k = k % len(nums)
	if k == 0 {
		return
	}

	for i := 0; i < len(nums)/2; i++ {
		nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
	}

	for i := 0; i < k/2; i++ {
		nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
	}
	for i := 0; i < (len(nums)-k)/2; i++ {
		nums[i+k], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i+k]
	}
}

// Time complexity: O(n) where n is the length of nums
// Space complexity: O(n)
func rotate2(nums []int, k int) {
	k = k % len(nums)
	if k == 0 {
		return
	}

	tail := make([]int, 0, k)
	for i := len(nums) - k; i < len(nums); i++ {
		tail = append(tail, nums[i])
	}

	head := make([]int, 0, len(nums)-k)
	for i := 0; i < len(nums)-k; i++ {
		head = append(head, nums[i])
	}

	for i, el := range tail {
		nums[i] = el
	}
	for i, el := range head {
		nums[i+k] = el
	}
}
