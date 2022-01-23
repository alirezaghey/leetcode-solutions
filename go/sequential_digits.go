package leetcode

import (
	"math"
	"sort"
	"strconv"
)

func sequentialDigits(low int, high int) []int {
	lowD, highD := int(math.Log10(float64(low)))+1, int(math.Log10(float64(high)))+1
	res := make([]int, 0, 10)
	base := "123456789"

	for length := lowD; length <= highD; length++ {
		for start := 0; start <= 9-length; start++ {
			num, _ := strconv.Atoi(base[start : start+length])
			if num >= low && num <= high {
				res = append(res, num)
			}
		}
	}
	return res
}

func sequentialDigits2(low int, high int) []int {
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
