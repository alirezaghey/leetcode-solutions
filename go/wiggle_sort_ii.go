package leetcode

import (
	"sort"
)

func wiggleSort(nums []int) {
	sort.Ints(nums)
	temp := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		temp[i] = nums[i]
	}

	j := len(nums) - 1
	for i := 1; i < len(nums); i, j = i+2, j-1 {
		nums[i] = temp[j]
	}

	for i := 0; i < len(nums); i, j = i+2, j-1 {
		nums[i] = temp[j]
	}
}

// func wiggleSort(nums []int)  {
//     sort.Sort(Integers(nums))
//     temp := make([]int, len(nums))
//     for i := 0; i < len(nums); i++ {
//         temp[i] = nums[i]
//     }
//
//     j := len(nums)-1
//     for i := 1; i < len(nums); i, j = i+2, j-1 {
//         nums[i] = temp[j]
//     }
//
//     for i := 0; i < len(nums); i, j = i+2, j-1 {
//         nums[i] = temp[j]
//     }
//
//
// }
//
// type Integers []int;
//
// func (x Integers) Len() int {return len(x)}
// func (x Integers) Less(i, j int) bool {return x[i] < x[j]}
// func (x Integers) Swap(i, j int) {x[i], x[j] = x[j], x[i]}
