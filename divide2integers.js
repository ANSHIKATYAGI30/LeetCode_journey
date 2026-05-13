/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {

    const INT_MAX = 2147483647;
    const INT_MIN = -2147483648;

    // Overflow case
    if(dividend === INT_MIN && divisor === -1) {
        return INT_MAX;
    }

    // Determine sign
    let negative =
        (dividend < 0) !== (divisor < 0);

    // Convert to positive
    let a = Math.abs(dividend);
    let b = Math.abs(divisor);

    let result = 0;
  
    while(a >= b) {
        let temp = b;
        let multiple = 1;
        // Double divisor
        while(a >= (temp << 1)) {
            temp <<= 1;
            multiple <<= 1;
        }
        a -= temp;
        result += multiple;
    }

    return negative ? -result : result;
};
