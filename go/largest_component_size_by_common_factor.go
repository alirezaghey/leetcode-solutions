package leetcode

import (
	"math"
)

func largestComponentSize(nums []int) int {
	n := len(nums)

	connectionDict := make(map[int][]int)
	uf := UnionFind{}
	uf.data = make([]int, n)
	for i := 0; i < n; i++ {
		uf.data[i] = i
	}

	for i, el := range nums {
		factors := find_factors(el, make(map[int]bool))
		for factor, _ := range factors {
			if _, ok := connectionDict[factor]; !ok {
				connectionDict[factor] = make([]int, 0)
			}
			connectionDict[factor] = append(connectionDict[factor], i)
		}
	}

	for _, indices := range connectionDict {
		for i := 0; i < len(indices)-1; i++ {
			uf.union(indices[i], indices[i+1])
		}
	}

	counter := make(map[int]int)
	for i := 0; i < n; i++ {
		p := uf.find(i)
		if _, ok := counter[p]; !ok {
			counter[p] = 1
		} else {
			counter[p] += 1
		}
	}

	res := 0
	for _, v := range counter {
		if v > res {
			res = v
		}
	}
	return res

}

func find_factors(n int, m map[int]bool) map[int]bool {
	for i := 2; i < int(math.Floor(math.Sqrt(float64(n))))+1; i++ {
		if n%i == 0 {
			m[i] = true
			find_factors(n/i, m)
			return m
		}
	}
	m[n] = true
	return m
}

type UnionFind struct {
	data []int
}

func (uf UnionFind) find(x int) int {
	if uf.data[x] != x {
		uf.data[x] = uf.find(uf.data[x])
	}
	return uf.data[x]
}

func (uf UnionFind) union(x, y int) {
	xp, yp := uf.find(x), uf.find(y)
	uf.data[xp] = yp
}
