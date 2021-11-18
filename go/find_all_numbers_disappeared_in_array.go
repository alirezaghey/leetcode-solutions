package leetcode

// inplace, O(n) time, O(1) space
func findDisappearedNumbers(nums []int) []int {
	for _, el := range nums {
		var idx int
		if el < 0 {
			idx = -el
		} else {
			idx = el
		}
		if nums[idx-1] > 0 {
			nums[idx-1] *= -1
		}
	}
	var res []int
	for i, el := range nums {
		if el > 0 {
			res = append(res, i+1)
		}
	}
	return res
}

// using an map, O(n) time, O(n) space
// func findDisappearedNumbers(nums []int) []int {
//     dic := make(map[int]bool)
//
//     for _, el := range nums {
//         dic[el] = true
//     }
//     var res []int
//     for i := 1; i < len(nums)+1; i++ {
//         _, ok := dic[i]
//         if ok != true {
//             res = append(res, i)
//         }
//     }
//     return res
// }
