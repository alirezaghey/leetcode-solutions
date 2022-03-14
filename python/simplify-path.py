class Solution:
    # Time complexity: O(n) where n the length of the input string is
    # Space complexity: O(n)
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        res = []
        
        for p in path:
            if not p or p == ".": continue
            if p == "..":
                if res:
                    res.pop()
            else:
                res.append(p)
                
        return "/" + "/".join(res)