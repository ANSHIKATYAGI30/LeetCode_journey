/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    for(let ch of s) {
        // Opening brackets
        if(ch === '(' || ch === '[' || ch === '{') {
            stack.push(ch);
        }
        // Closing brackets
        else {
            // Stack empty
            if(stack.length === 0) {
                return false;
            }
            let top = stack.pop();
            // Check matching
            if(
                (ch === ')' && top !== '(') ||
                (ch === ']' && top !== '[') ||
                (ch === '}' && top !== '{')
            ) {
                return false;
            }
        }
    }

    // Valid only if stack empty
    return stack.length === 0;
};
