package leetcode

import (
	"strings"
)

func solveNQueens(n int) [][]string {
	res := make([][]string, 0)
	backtrack(make(map[int]bool), make(map[int]bool), make(map[int]bool), n, make([]int, 0), &res)
	return res
}

func backtrack(rows map[int]bool, diags map[int]bool, antiDiags map[int]bool, n int, partialRes []int, res *[][]string) {
	if len(partialRes) >= n {
		*res = append(*res, writeOutNQueens(partialRes, n))
	}

	c := len(partialRes)
	for r := 0; r < n; r++ {
		_, ok := rows[r]
		_, ok2 := diags[r-c]
		_, ok3 := antiDiags[r+c]
		if !ok && !ok2 && !ok3 {
			rows[r], diags[r-c], antiDiags[r+c] = true, true, true
			partialRes = append(partialRes, r)
			backtrack(rows, diags, antiDiags, n, partialRes, res)
			partialRes = partialRes[:len(partialRes)-1]
			delete(rows, r)
			delete(diags, r-c)
			delete(antiDiags, r+c)
		}
	}
}

func writeOutNQueens(arr []int, n int) []string {
	res := make([]string, 0, n)

	for _, el := range arr {
		res = append(res, strings.Repeat(".", el)+"Q"+strings.Repeat(".", n-el-1))
	}
	return res
}
