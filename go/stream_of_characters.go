package leetcode

type StreamChecker struct {
	root   TrieNode
	stream []byte
}

type TrieNode struct {
	node map[byte]TrieNode
}

func Constructor(words []string) StreamChecker {
	streamChecker := StreamChecker{TrieNode{make(map[byte]TrieNode)}, make([]byte, 0, 100)}

	for _, word := range words {
		node := streamChecker.root.node
		for i := len(word) - 1; i >= 0; i-- {
			c := word[i]
			if _, ok := node[c]; !ok {
				node[c] = TrieNode{make(map[byte]TrieNode)}
			}
			node = node[c].node
		}
		if _, ok := node['#']; !ok {
			node['#'] = TrieNode{make(map[byte]TrieNode)}
		}
	}
	return streamChecker
}

func (this *StreamChecker) Query(letter byte) bool {
	this.stream = append(this.stream, letter)
	node := this.root.node

	for i := len(this.stream) - 1; i >= 0; i-- {
		c := this.stream[i]
		if _, ok := node['#']; ok {
			return true
		} else if nextNode, ok := node[c]; ok {
			node = nextNode.node
		} else {
			return false
		}
	}
	if _, ok := node['#']; ok {
		return true
	}
	return false
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.Query(letter);
 */
