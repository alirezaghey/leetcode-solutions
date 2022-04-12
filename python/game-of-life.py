from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        temp = [row[:] for row in board]

        def number_of_living_neighs(r, c):
            return sum(temp[r+rr][c+cc] if 0 <= r+rr < R and 0 <= c+cc < C and (rr != 0 or cc != 0) else 0 for rr in range(-1, 2) for cc in range(-1, 2))

        for r in range(R):
            for c in range(C):
                num_living = number_of_living_neighs(r, c)
                if board[r][c]:  # is alive
                    if 2 <= num_living <= 3:
                        continue
                    board[r][c] = 0
                else:  # dead
                    if num_living == 3:
                        board[r][c] = 1
