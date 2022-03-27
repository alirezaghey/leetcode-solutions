from typing import List


class Solution:
    # Time complexity: O(max(n * log n, n*m))
    # where n and m equal the number of rows and columns in the matrix
    # Space complexity: O(n)
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for i, el in sorted(((i, sum(row)) for i, row in enumerate(mat)), key=lambda x: (x[1], x[0]))][:k]
