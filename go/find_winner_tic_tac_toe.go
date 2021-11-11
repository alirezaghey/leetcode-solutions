package leeetcode

func tictactoe(moves [][]int) string {
	check_rows := func(game_board [3][3]string, char string) bool {
		for _, row := range game_board {
			if row[0] == char && row[1] == char && row[2] == char {
				return true
			}
		}
		return false
	}

	check_cols := func(game_board [3][3]string, char string) bool {
		for i := 0; i < 3; i++ {
			if game_board[0][i] == char && game_board[1][i] == char && game_board[2][i] == char {
				return true
			}
		}
		return false
	}

	check_diags := func(game_board [3][3]string, char string) bool {
		if game_board[0][0] == char && game_board[1][1] == char && game_board[2][2] == char {
			return true
		} else if game_board[0][2] == char && game_board[1][1] == char && game_board[2][0] == char {
			return true
		}
		return false
	}

	var game_board [3][3]string
	alex := true

	for _, el := range moves {
		if alex == true {
			game_board[el[0]][el[1]] = "X"
		} else {
			game_board[el[0]][el[1]] = "O"
		}
		alex = !alex
	}

	if check_rows(game_board, "X") || check_cols(game_board, "X") || check_diags(game_board, "X") {
		return "A"
	}
	if check_rows(game_board, "O") || check_cols(game_board, "O") || check_diags(game_board, "O") {
		return "B"
	}

	for _, row := range game_board {
		for _, cell := range row {
			if cell == "" {
				return "Pending"
			}
		}
	}

	return "Draw"
}
