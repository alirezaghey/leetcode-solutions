package leetcode

import (
	"sort"
)

func accountsMerge(accounts [][]string) [][]string {
	uf := UnionFind{make([]int, len(accounts)), make([]int, len(accounts))}
	for i := 0; i < len(accounts); i++ {
		uf.Roots[i] = i
		uf.Ranks[i] = 1
	}

	mappedAccounts := make([]map[string]bool, len(accounts))
	for i, account := range accounts {
		m := make(map[string]bool)
		for j := 1; j < len(account); j++ {
			m[account[j]] = true
		}
		mappedAccounts[i] = m
	}

	for i := 0; i < len(mappedAccounts); i++ {
		for j := i + 1; j < len(mappedAccounts); j++ {
			for key := range mappedAccounts[i] {
				if _, ok := mappedAccounts[j][key]; ok == true {
					uf.Union(i, j)
				}
			}
		}
	}

	mergedAccounts := make(map[int]map[string]bool)
	for i, m := range mappedAccounts {
		root := uf.Find(i)
		if _, ok := mergedAccounts[root]; ok == false {
			mergedAccounts[root] = make(map[string]bool)
		}
		val, _ := mergedAccounts[root]
		for key := range m {
			val[key] = true
		}
	}

	res := make([][]string, len(mergedAccounts))
	i := 0
	for root, m := range mergedAccounts {
		sortedEmails := make([]string, len(m))
		j := 0
		for key := range m {
			sortedEmails[j] = key
			j++
		}
		sort.Strings(sortedEmails)
		sortedEmailsWithName := make([]string, len(sortedEmails)+1)
		sortedEmailsWithName[0] = accounts[root][0]
		for j = 0; j < len(sortedEmails); j++ {
			sortedEmailsWithName[j+1] = sortedEmails[j]
		}
		res[i] = sortedEmailsWithName
		i++
	}
	return res
}

type UnionFind struct {
	Roots []int
	Ranks []int
}

func (uf UnionFind) Find(x int) int {
	for x != uf.Roots[x] {
		uf.Roots[x] = uf.Roots[uf.Roots[x]]
		x = uf.Roots[x]
	}
	return x
}

func (uf UnionFind) Union(x, y int) bool {
	rootX, rootY := uf.Find(x), uf.Find(y)
	if uf.Roots[x] == uf.Roots[y] {
		return true
	}

	if uf.Ranks[rootX] > uf.Ranks[rootY] {
		uf.Roots[rootY] = rootX
	} else if uf.Ranks[rootY] > uf.Ranks[rootX] {
		uf.Roots[rootX] = rootY
	} else {
		uf.Ranks[rootX] += 1
		uf.Roots[rootY] = rootX
	}
	return false
}
