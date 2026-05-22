/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    
    let rows = new Set();
    let cols = new Set();
    let boxes = new Set();

    for (let i = 0; i < 9; i++) {

        for (let j = 0; j < 9; j++) {

            let num = board[i][j];

            if (num === ".") continue;

            let rowKey = `${i}-${num}`;
            let colKey = `${j}-${num}`;
            let boxKey = `${Math.floor(i / 3)}-${Math.floor(j / 3)}-${num}`;

            if (
                rows.has(rowKey) ||
                cols.has(colKey) ||
                boxes.has(boxKey)
            ) {
                return false;
            }

            rows.add(rowKey);
            cols.add(colKey);
            boxes.add(boxKey);
        }
    }

    return true;
};
