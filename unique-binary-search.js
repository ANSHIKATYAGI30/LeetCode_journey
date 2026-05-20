/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    
    let dp = new Array(n + 1).fill(0);

    dp[0] = 1;
    dp[1] = 1;

    for (let nodes = 2; nodes <= n; nodes++) {

        for (let root = 1; root <= nodes; root++) {

            let left = dp[root - 1];
            let right = dp[nodes - root];

            dp[nodes] += left * right;
        }
    }

    return dp[n];
};
