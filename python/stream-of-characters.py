from typing import List

class StreamChecker:

    def __init__(self, words: List[str]):
        self.rev_trie = self.create_rev_trie(words)
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        return self.find()
    
    def create_rev_trie(self, words):
        root = {}
        for word in words:
            node = root
            for i in range(len(word)-1, -1, -1):
                if word[i] not in node:
                    node[word[i]] = {}
                node = node[word[i]]
            node['#'] = True
        return root
    
    def find(self):
        node = self.rev_trie
        for i in range(len(self.stream)-1, -1, -1):
            if self.stream[i] in node:
                node = node[self.stream[i]]
                if '#' in node: return True
            else:
                return False
        return False