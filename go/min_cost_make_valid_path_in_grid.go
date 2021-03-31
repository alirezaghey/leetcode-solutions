package leetcode

import (
	"container/list"
	"strconv"
)

func minCost(grid [][]int) int {
	RIGHT, LEFT, DOWN, UP := 1, 2, 3, 4
	R, C := len(grid), len(grid[0])
	dirs := [][]int{{-1, 0, UP}, {0, 1, RIGHT}, {1, 0, DOWN}, {0, -1, LEFT}}

	best := (1 << 31) - 1
	dic := make(map[string]int)
	dic["0,0"] = 0
	deq := list.New()
	deq.PushBack(Node{0, 0, 0})

	for deq.Len() > 0 {
		el := deq.Front()
		deq.Remove(el)
		node := el.Value.(Node)
		r, c, cost := node.r, node.c, node.cost

		if r == R-1 && c == C-1 {
			if cost < best {
				best = cost
			}
			continue
		}
		for _, next := range dirs {
			dr, dc, d := next[0], next[1], next[2]
			nr, nc := r+dr, c+dc
			if nr < 0 || nr >= R || nc < 0 || nc >= C {
				continue // coords out of bounds
			}
			var ncost int
			if grid[r][c] == d {
				ncost = cost
			} else {
				ncost = cost + 1
			}
			key := strconv.Itoa(nr) + "," + strconv.Itoa(nc)
			if val, ok := dic[key]; ok && val <= ncost {
				continue // already visited with lower cost
			}
			dic[key] = ncost
			deq.PushBack(Node{nr, nc, ncost})
		}
	}
	return best
}

type Node struct {
	r, c, cost int
}
