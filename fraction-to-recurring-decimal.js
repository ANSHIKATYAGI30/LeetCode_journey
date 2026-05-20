/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    
    if (numerator === 0) return "0";

    let result = "";

    // Handle sign
    if ((numerator < 0) ^ (denominator < 0)) {
        result += "-";
    }

    let num = Math.abs(numerator);
    let den = Math.abs(denominator);

    // Integer part
    result += Math.floor(num / den);

    let rem = num % den;

    if (rem === 0) {
        return result;
    }

    result += ".";

    // Store remainder positions
    let map = new Map();

    while (rem !== 0) {

        // Repeating remainder found
        if (map.has(rem)) {

            let index = map.get(rem);

            result =
                result.slice(0, index) +
                "(" +
                result.slice(index) +
                ")";

            break;
        }
        map.set(rem, result.length);
        rem *= 10;
        result += Math.floor(rem / den);
        rem %= den;
    }

    return result;
};
