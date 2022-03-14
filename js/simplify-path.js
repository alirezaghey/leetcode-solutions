/**
 * @param {string} path
 * @return {string}
 */
// Time complexity: O(n) where n the length of path is
// Space complexity: O(n)
var simplifyPath = function(path) {
    path = path.split("/")
    const res = []
    
    for (p of path) {
        if (p === "" || p === ".") continue
        if (p == "..") {
            if (res.length > 0) res.pop()
        } else {
            res.push(p)
        }
    }
    return "/" + res.join("/")
};