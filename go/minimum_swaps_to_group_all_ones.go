package leetcode

func minSwaps(nums []int) int {
	ones := sum(nums)
	nums = append(nums, nums...)

	maxOnesWindow := sum(nums[:ones])
	currOnesWindow := maxOnesWindow

	left, right := 0, ones-1
	for i := 0; i < len(nums)-ones; i++ {
		if nums[left+i] == 1 {
			currOnesWindow -= 1
		}
		if nums[right+i+1] == 1 {
			currOnesWindow += 1
		}
		maxOnesWindow = max(maxOnesWindow, currOnesWindow)
	}
	return ones - maxOnesWindow
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func sum(nums []int) int {
	res := 0
	for _, el := range nums {
		res += el
	}
	return res
}
