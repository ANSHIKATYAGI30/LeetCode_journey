/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    const memo = {};
    function dp(i, j) {
        const key = i + "," + j;
        if(key in memo) {
            return memo[key];
        }
        // Pattern finished
        if(j === p.length) {
            return i === s.length;
        }
        // Current characters match?
        const firstMatch =
            i < s.length &&
            (s[i] === p[j] || p[j] === '.');
        let ans;
        // Next char is '*'
        if(j + 1 < p.length && p[j + 1] === '*') {
            ans =
                dp(i, j + 2) ||                  // skip x*
                (firstMatch && dp(i + 1, j));   // use x*
        }
        else {
            ans = firstMatch && dp(i + 1, j + 1);
        }
        memo[key] = ans;

        return ans;
    }

    return dp(0, 0);
};
