package leetcode

func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
	res := make([][]int, 0)
	i, j := 0, 0

	for i < len(firstList) && j < len(secondList) {
		if (firstList[i][1] >= secondList[j][0] && firstList[i][1] <= secondList[j][1]) ||
			(secondList[j][1] >= firstList[i][0] && secondList[j][1] <= firstList[i][1]) {
			start, end := 0, 0
			if firstList[i][0] > secondList[j][0] {
				start = firstList[i][0]
			} else {
				start = secondList[j][0]
			}
			if firstList[i][1] < secondList[j][1] {
				end = firstList[i][1]
			} else {
				end = secondList[j][1]
			}
			res = append(res, []int{start, end})
		}
		if firstList[i][1] < secondList[j][1] {
			i += 1
		} else {
			j += 1
		}
	}
	return res
}
