class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = list(characters)
        self.length = combinationLength
        self.idx = 0
        self.combinations = []
        
        def backtrack(idx, partial_res):
            if len(partial_res) == self.length:
                self.combinations.append("".join(partial_res))
                return
            
            for i in range(idx, len(self.chars)):
                partial_res.append(self.chars[i])
                backtrack(i+1, partial_res)
                partial_res.pop()
        backtrack(0, [])
        
    def next(self) -> str:
        self.idx +=1
        return self.combinations[self.idx-1]

    def hasNext(self) -> bool:
        return self.idx < len(self.combinations)