class WordDictionary:

    def __init__(self):
        self.trie = {} 

    # Time complexity: O(n) where n is the length of word
    # Space complexity: O(n)
    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = {}

    # Time complexity: O(max(26^m, n)) where m is the number of `.` in the searched word and n is the length of the searched word
    # Space complexity: O(m) where m is the number of `.` in the searched word
    def search(self, word: str) -> bool:
        def search_helper(word, node):
            for i, c in enumerate(word):
                if c == ".":
                    rest_word = word[i+1:]
                    return any(search_helper(rest_word, node[neighbor]) for neighbor in node)
                elif c in node:
                    node = node[c]
                else:
                    return False
            return "#" in node
        return search_helper(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)