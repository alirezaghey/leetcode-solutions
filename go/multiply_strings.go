package leetcode

import (
	"strconv"
	"strings"
)

func multiply(num1 string, num2 string) string {
	product := make([]int, len(num1)+len(num2))
	pos := len(product) - 1

	for i := len(num1) - 1; i >= 0; i-- {
		temp_pos := pos
		for j := len(num2) - 1; j >= 0; j-- {
			n1 := int(num1[i] - '0')
			n2 := int(num2[j] - '0')
			product[temp_pos] += n1 * n2
			product[temp_pos-1] += product[temp_pos] / 10
			product[temp_pos] = product[temp_pos] % 10
			temp_pos -= 1
		}
		pos -= 1
	}
	ptr := 0
	for ptr < len(product)-1 && product[ptr] == 0 {
		ptr += 1
	}
	var res strings.Builder
	res.Grow(len(product))
	for ; ptr < len(product); ptr++ {
		res.WriteString(strconv.Itoa(product[ptr]))
	}
	return res.String()

}
