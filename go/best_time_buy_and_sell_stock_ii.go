package leetcode

func maxProfit(prices []int) int {
	res, curr := 0, prices[0]

	for i := 1; i < len(prices); i++ {
		if prices[i] < curr {
			curr = prices[i]
		} else {
			res += prices[i] - curr
			curr = prices[i]
		}
	}
	return res
}
