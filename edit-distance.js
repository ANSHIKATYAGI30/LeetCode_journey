/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    
    let m = word1.length;
    let n = word2.length;

    // dp[i][j] = min operations to convert
    // word1[0...i-1] -> word2[0...j-1]
    let dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

    // Base cases
    for (let i = 0; i <= m; i++) {
        dp[i][0] = i; // delete all chars
    }

    for (let j = 0; j <= n; j++) {
        dp[0][j] = j; // insert all chars
    }

    // Fill DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {

            // Characters match
            if (word1[i - 1] === word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } 
            else {
                dp[i][j] = 1 + Math.min(
                    dp[i - 1][j],     // delete
                    dp[i][j - 1],     // insert
                    dp[i - 1][j - 1]  // replace
                );
            }
        }
    }

    return dp[m][n];
};
