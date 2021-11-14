package leetcode

type CombinationIterator struct {
	idx          int
	combinations []string
}

func Constructor(characters string, combinationLength int) CombinationIterator {
	iterator := CombinationIterator{
		idx:          0,
		combinations: make([]string, 0),
	}
	var backtrack func(curr string, chars []rune)

	backtrack = func(curr string, chars []rune) {
		if len(curr) == combinationLength {
			iterator.combinations = append(iterator.combinations, curr)
			return
		}

		for i, c := range chars {
			backtrack(curr+string(c), chars[i+1:])
		}
	}
	backtrack("", []rune(characters))
	return iterator
}

func (this *CombinationIterator) Next() string {
	this.idx += 1
	return this.combinations[this.idx-1]
}

func (this *CombinationIterator) HasNext() bool {
	return this.idx < len(this.combinations)
}
