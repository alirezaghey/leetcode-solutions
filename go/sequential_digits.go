package leetcode

import (
	"sort"
)

func sequentialDigits(low int, high int) []int {
	var backtrack func(int, int)
	res := make([]int, 0)
	backtrack = func(num, curr int) {
		if num > 9 {
			return
		}
		curr = curr*10 + num
		if curr >= low {
			if curr > high {
				return
			} else {
				res = append(res, curr)
			}
		}
		backtrack(num+1, curr)
	}

	for i := 1; i < 10; i++ {
		backtrack(i+1, i)
	}
	sort.Ints(res)
	return res
}
