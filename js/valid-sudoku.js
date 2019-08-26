// Related Topics: Hash Table
// Difficulty: Medium

/*
Initial thoughts:
Using a Set we are going to check whether there are any duplicate
numbers among the rows, columns, or 3*3 squares and return true
or false based on that.

Time complexity: O(1) since the input is of fixed length (a sudoku board) the time complexity is fixed.
Space complexity: O(1) since the input is constant the auxiliary space that we use is also constant

*/

/**
 * @param {character[][]} board
 * @return {boolean}
 */
const isValidSudoku = board => {
  // Checking the rows for validity
  if (
    board.some(row => {
      const filteredRow = row.filter(el => el !== '.');
      if (filteredRow.length !== new Set(filteredRow).size) return true;
    })
  )
    return false;

  // Checking columns for validity
  if (
    board[0]
      .map((_, i) => {
        return board.map((_, j) => board[j][i]);
      })
      .some(col => {
        const filteredCol = col.filter(el => el !== '.');
        if (filteredCol.length !== new Set(filteredCol).size) return true;
      })
  ) {
    return false;
  }

  // Checking squares for validity
  for (let i = 0; i < board.length; i += 3) {
    for (let j = 0; j < board[0].length; j += 3) {
      const tempSquare = [];
      for (let k = 0; k < 3; k++) {
        for (let l = 0; l < 3; l++) {
          if (board[i + k][j + l] !== '.') tempSquare.push(board[i + k][j + l]);
        }
      }
      if (tempSquare.length !== new Set(tempSquare).size) return false;
    }
  }
  return true;
};
