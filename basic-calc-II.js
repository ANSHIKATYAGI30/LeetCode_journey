/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    let stack = [];
    let num = 0;
    let sign = '+';

    for (let i = 0; i < s.length; i++) {
        let ch = s[i];

        if (ch >= '0' && ch <= '9') {
            num = num * 10 + (ch - '0');
        }

        // Process when operator OR last character
        if ((ch < '0' || ch > '9') && ch !== ' ' || i === s.length - 1) {

            if (sign === '+') {
                stack.push(num);
            } 
            else if (sign === '-') {
                stack.push(-num);
            } 
            else if (sign === '*') {
                stack.push(stack.pop() * num);
            } 
            else if (sign === '/') {
                let prev = stack.pop();

                // truncate toward zero
                stack.push(prev / num > 0 
                    ? Math.floor(prev / num)
                    : Math.ceil(prev / num));
            }

            sign = ch;
            num = 0;
        }
    }

    return stack.reduce((a, b) => a + b, 0);
};
