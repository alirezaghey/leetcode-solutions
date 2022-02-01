package leetcode

// Time complexity: O(n) wheere n is the length of prices
// Space complexity: O(1)
func maxProfit(prices []int) int {
	min_price, max_profit := int(^uint(0)>>1), 0

	for _, el := range prices {
		max_profit = max(max_profit, el-min_price)
		min_price = min(min_price, el)
	}
	return max_profit

}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
