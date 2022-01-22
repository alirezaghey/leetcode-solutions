package leetcode

// Time complexity: O(n) where n is the length of gas array
// Space complexity: O(1)
func canCompleteCircuit(gas []int, cost []int) int {
	total, curr, res := 0, 0, 0
	for i, el := range gas {
		total += el - cost[i]
		curr += el - cost[i]
		if curr < 0 {
			curr = 0
			res = i + 1
		}
	}
	if total >= 0 {
		return res
	} else {
		return -1
	}

}

// Time complexity: O(n^2) where n is the length of gas array
// Space complexity: O(1)
// Note: TLE
func canCompleteCircuit2(gas []int, cost []int) int {
	for i := 0; i < len(gas); i++ {
		curr := gas[i] - cost[i]
		j := (i + 1) % len(gas)
		for ; j != i; j = (j + 1) % len(gas) {
			if curr < 0 {
				break
			}
			curr += gas[j] - cost[j]
		}
		if i == j && curr >= 0 {
			return i
		}
	}
	return -1
}
