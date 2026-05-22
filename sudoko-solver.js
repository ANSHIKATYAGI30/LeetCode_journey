/**
 * @param {character[][]} board
 * @return {void}
 */
var solveSudoku = function(board) {

    function isValid(board, row, col, num) {

        // Check row
        for (let j = 0; j < 9; j++) {
            if (board[row][j] === num) {
                return false;
            }
        }

        // Check column
        for (let i = 0; i < 9; i++) {
            if (board[i][col] === num) {
                return false;
            }
        }

        // Check 3x3 box
        let startRow = Math.floor(row / 3) * 3;
        let startCol = Math.floor(col / 3) * 3;

        for (let i = startRow; i < startRow + 3; i++) {

            for (let j = startCol; j < startCol + 3; j++) {

                if (board[i][j] === num) {
                    return false;
                }
            }
        }

        return true;
    }

    function solve(board) {

        for (let i = 0; i < 9; i++) {

            for (let j = 0; j < 9; j++) {

                if (board[i][j] === ".") {

                    for (let num = 1; num <= 9; num++) {

                        let char = num.toString();

                        if (isValid(board, i, j, char)) {

                            board[i][j] = char;

                            if (solve(board)) {
                                return true;
                            }

                            // Backtrack
                            board[i][j] = ".";
                        }
                    }

                    return false;
                }
            }
        }

        return true;
    }

    solve(board);
};
