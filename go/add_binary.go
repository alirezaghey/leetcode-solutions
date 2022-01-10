package leetcode

func addBinary(a string, b string) string {
	ra := []rune(a)
	rb := []rune(b)
	res := make([]int, 0)
	carry, i, j := 0, len(ra)-1, len(rb)-1

	for i >= 0 || j >= 0 {
		curr := carry
		if i >= 0 {
			curr += int(ra[i]) - 48
			i -= 1
		}
		if j >= 0 {
			curr += int(rb[j]) - 48
			j -= 1
		}
		res = append(res, curr%2)
		carry = curr / 2
	}
	if carry == 1 {
		res = append(res, 1)
	}
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}

	rRes := make([]rune, len(res))
	for i, el := range res {
		if el == 1 {
			rRes[i] = '1'
		} else {
			rRes[i] = '0'
		}
	}
	return string(rRes)
}
