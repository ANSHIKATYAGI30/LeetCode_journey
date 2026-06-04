/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var totalWaviness = function(num1, num2) {

    // returns waviness of one number
    function getWaviness(num) {
        let s = num.toString();

        // numbers with < 3 digits => 0
        if (s.length < 3) return 0;

        let count = 0;

        // check every middle digit
        for (let i = 1; i < s.length - 1; i++) {
            let left = Number(s[i - 1]);
            let mid = Number(s[i]);
            let right = Number(s[i + 1]);

            // peak
            if (mid > left && mid > right) {
                count++;
            }

            // valley
            else if (mid < left && mid < right) {
                count++;
            }
        }

        return count;
    }

    let total = 0;

    // check every number in range
    for (let num = num1; num <= num2; num++) {
        total += getWaviness(num);
    }

    return total;
};
