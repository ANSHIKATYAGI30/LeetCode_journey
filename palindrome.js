/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {

    // Negative numbers cannot be palindrome
    if(x < 0) {
        return false;
    }

    let original = x;
    let reverse = 0;

    while(x > 0) {

        let digit = x % 10;

        reverse = reverse * 10 + digit;

        x = Math.floor(x / 10);
    }

    return original === reverse;
};
