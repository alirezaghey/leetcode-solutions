class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        game_board = [[""]*3 for _ in range(3)]
        Alex = True
        for r, c in moves:
            game_board[r][c] = "X" if Alex else "O"
            Alex = Alex ^ True
        
        def checkRows(game_board, char):
            for row in game_board:
                if "".join(row) == char*3:
                    return True
            return False
        def checkCols(game_board, char):
            for col in list(zip(*game_board)):
                print(col)
                if "".join(col) == char*3:
                    return True
            return False
        def checkDiag(game_board, char):
            return (
                "".join([game_board[i][i] for i in range(3)]) == char*3 or
                "".join([game_board[i][2-i] for i in range(3)]) == char*3
            )
        
        if checkRows(game_board, "X") or checkCols(game_board, "X") or checkDiag(game_board, "X"): return "A"
        if checkRows(game_board, "O") or checkCols(game_board, "O")or checkDiag(game_board, "O"): return "B"
        
        for row in game_board:
            for cell in row:
                if cell == "":
                    return "Pending"
        
        return "Draw"