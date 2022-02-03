package leetcode

// Time complexity: O(n^2) where n is the length of nums
// Space complexity: O(n^2)
func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	dic := make(map[int]int)
	for _, x := range nums1 {
		for _, y := range nums2 {
			if _, ok := dic[x+y]; ok == true {
				dic[x+y] += 1
			} else {
				dic[x+y] = 1
			}
		}
	}

	res := 0
	for _, x := range nums3 {
		for _, y := range nums4 {
			if val, ok := dic[-(x + y)]; ok == true {
				res += val
			}
		}
	}
	return res
}
