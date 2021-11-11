package leetcode

func arrangeCoins(n int) int {
	left, right, res := 1, n, 1

	for left <= right {
		mid := left + (right-left)/2

		if mid*(mid+1)/2 <= n {
			if res < mid {
				res = mid
			}
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return res
}

/*
O(n) solution
func arrangeCoins(n int) int {
    res, i := 0, 1

    for i <= n {
        res += 1
        n -= i
        i += 1
    }
    return res
}
*/
