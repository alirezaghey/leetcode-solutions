package leetcode

// Time complexity: O(n * m) where n and m are the number of clients and banks
// Space complexity: O(1)
func maximumWealth(accounts [][]int) int {
	res := 0
	for _, client := range accounts {
		res = max(res, sum(client))
	}
	return res
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func maxArr(arr []int) int {
	res := arr[0]
	for _, el := range arr {
		res = max(res, el)
	}
	return res
}

func sum(arr []int) int {
	res := 0
	for _, el := range arr {
		res += el
	}
	return res
}
