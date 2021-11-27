package leetcode

func productExceptSelf(nums []int) []int {
	res := make([]int, len(nums))
	res[len(res)-1] = 1

	for i := len(nums) - 2; i >= 0; i-- {
		res[i] = res[i+1] * nums[i+1]
	}

	curr := 1
	for i := 0; i < len(nums); i++ {
		res[i] *= curr
		curr *= nums[i]
	}

	return res
}
