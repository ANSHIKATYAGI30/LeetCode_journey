/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {

    let candidate = null;
    let count = 0;

    for(let num of nums) {

        // Choose new candidate
        if(count === 0) {
            candidate = num;
        }

        // Increase or decrease count
        if(num === candidate) {
            count++;
        }
        else {
            count--;
        }
    }

    return candidate;
};
