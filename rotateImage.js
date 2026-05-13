/**
 * @param {number[][]} matrix
 * @return {void}
 */
var rotate = function(matrix) {

    let n = matrix.length;

    // Step 1: Transpose
    for(let i = 0; i < n; i++) {

        for(let j = i; j < n; j++) {

            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    // Step 2: Reverse each row
    for(let i = 0; i < n; i++) {

        matrix[i].reverse();
    }
};
