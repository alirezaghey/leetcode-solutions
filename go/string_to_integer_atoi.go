package leetcode

import (
	"math"
	"strings"
)

func myAtoi(s string) int {
	s = strings.Trim(s, " ")
	sRunes := []rune(s)

	if len(sRunes) == 0 {
		return 0
	}
	var sign int
	if sRunes[0] == '-' {
		sign = -1
		sRunes = sRunes[1:]
	} else if sRunes[0] == '+' {
		sign = 1
		sRunes = sRunes[1:]
	} else {
		sign = 1
	}

	res := 0
	Upper, Lower := int(math.Pow(2, 31))-1, -int(math.Pow(2, 31))
	for i := 0; i < len(sRunes) && sRunes[i] >= 48 && sRunes[i] <= 57; i++ {
		res *= 10
		res += int(sRunes[i]) - 48
		if res*sign < Lower {
			return Lower
		} else if res*sign > Upper {
			return Upper
		}
	}

	res *= sign
	if res < int(-math.Pow(2, 31)) {
		return -int(math.Pow(2, 31))
	} else if res > int(math.Pow(2, 31))-1 {
		return int(math.Pow(2, 31)) - 1
	} else {
		return res
	}
}
